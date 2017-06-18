'''
Problem: https://www.hackerrank.com/challenges/battery
Solved: True

Notes:  When looking at the training data we saw that after 4 hours of charging the batterylife was always 8 hours. 
        Therefor we could use a linear regression algorithm that was actually able to fit this data perfectly below 4 hours.
'''

import sys

def calcMean(x):
    return sum(x)/len(x)

def calcStDev(pop, mean):
    return sum([(x-mean)**2 for x in pop])**0.5
    

def calcKPCoefficient(pop1, mean1, pop2, mean2):
    diff1 = [x-mean1 for x in pop1]
    diff2 = [x-mean2 for x in pop2]
    
    numerator = sum(x*y for x, y in zip(diff1, diff2))
    denominator = (sum(x**2 for x in diff1))**0.5 * (sum(x**2 for x in diff2))**0.5
    return numerator/denominator
    

def calcSlope(x, mean_x, y, mean_y):        
    coeff = calcKPCoefficient(x, mean_x, y, mean_y)
    st_dev_x = calcStDev(x, mean_x)
    st_dev_y = calcStDev(y, mean_y)
    
    return coeff*(st_dev_y/st_dev_x)

def calcIntercept(slope, mean_x, mean_y):
    return mean_y-(slope*mean_x)
    
def predictScore(x, y, predict_by):  
    mean_x = calcMean(x)
    mean_y = calcMean(y)
    slope = calcSlope(x, mean_x, y, mean_y)
    intercept = calcIntercept(slope, mean_x, mean_y)
    
    return round(slope*predict_by+intercept, 2)

charged = []
battery = []
timeCharged = float(input().strip())
file = open("trainingdata.txt", "r")
for x in file.readlines():
    ch_bat = x.split(',')
    if float(ch_bat[0]) < 4:
        charged.append(float(ch_bat[0]))
        battery.append(float(ch_bat[1]))

if timeCharged < 4:
    print(predictScore(charged, battery, timeCharged))
else:
    print(8.00)