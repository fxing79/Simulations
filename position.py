# -*- coding: utf-8 -*-
"""
a simulator of game with positive expectation of gain, different position
@f.z.x 2016
"""

import pylab
import random

r_win=1 #赢赔率
r_loss=0.65 #输赔率
p=0.5 #赢概率
cap=[100]#初始资金
position=[0.5,1.0,1.5] #投注仓位
idx=range(0,100)

for exp in range(0,3):
    
    f=position[exp]
        
    for times in range(1,50):
        round=0
        del cap[1:len(cap)]
        for i in range(1,100):
            investment=cap[round]*f
            hold=cap[round]-investment
            dice=random.random()
            if dice<p:
                cap.append(hold+investment*(1+r_win))
            else: cap.append(hold+investment*(1-r_loss))
            round+=1
        
        if exp==0:
            plot0, =pylab.plot(idx, cap, 'g')
        if exp==1:
            plot1, =pylab.plot(idx, cap, 'b')        
        if exp==2:
            plot2, =pylab.plot(idx, cap, 'r')
            
pylab.title('Simulator')
pylab.xlabel('rounds of play')
pylab.ylabel('capital (start w/ $100)')
#pylab.ylim(0, 1000)
pylab.legend([plot0, plot1, plot2], ["position=0.8","position=1.0","position=1.5"])

pylab.show()
