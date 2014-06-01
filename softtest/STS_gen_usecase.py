#!/bin/env python
# -*- coding=utf-8 -*-
import random
import sys


class pitch:
    def __init__(self, length=None, width=None):
        self.l = length
        self.w = width

    def __str__(self):
        res = "<begin pitch>\n%s<\end pitch>\n"
        length = "<length> %s <\length>\n" % self.l
        width = "<width> %s <\width>\n" % self.w
        if self.l != None and self.w != None:
            res = res % (length + width)
        elif self.l !=None and self.w == None:
            res = res % (length)
        elif self.l == None and self.w != None:
            res = res % (width)
        else:
            res = res % ''
        return res


class team:
    def __init__(self, name=None, num=None, stra=None):
        self.name = name
        self.num = num
        self.strategy = stra
        self.regions = []
        if self.strategy == "random":
            self.strategy = "<strategy> random\n<\strategy>"
        elif self.strategy == "custom":
            for i in range(self.num):
                a = []
                for j in range(4):
                    a.append(random.randint(1,100))
                region = "<region> (%s, %s) (%s, %s) <\\region>\n" % (a[0], a[1], a[2], a[3])
                self.regions.append(region)
            self.strategy = "<strategy> custom\n%s<\strategy>\n" % ''.join(self.regions)


    def __str__(self):
        res = "<begin team>\n%s%s%s<\end team>"
        if self.name == None:
            return res % ('', '', '')
        else:
            name = "<name> %s <\\name>\n" % self.name
        tnop = "<numberOfPlayers> %s <\\numberOfPlayers>\n" % self.num
        res = res % (name, tnop, self.strategy)
        return res
        




class STS:
    def __init__(self):
        self.names = ["SYSU", "SS", "SIST", "RMFC", "TEST"]
        self.lengths = [None, 120, 90, 75, 60, 100]
        self.widths = [None, 100, 90, 80, 75, 50]
        self.nops = [5,6,7,8,9,10,11,12,13]
        self.nots = [0,1,2,3,4,5,6,7,8,9]
        self.strategies = ["random", "custom"]
        
    def loop(self):
        nopts = random.randint(1,3)
        for i in range(nopts):
            print pitch(length=random.choice(self.lengths),width=random.choice(self.widths))
            numberOfTeam = random.choice(self.nots)
            for i in range(numberOfTeam):
                if i == 0:
                    print team()
                else:
                    print team(name=random.choice(self.names),num=random.choice(self.nops),stra=random.choice(self.strategies))
            print "\n"


if __name__ == "__main__":
    k = sys.stdin.readline()
    for i in range(int(k)):
        print "========Test Case %s========" % (i+1)
        sts = STS()
        sts.loop()

