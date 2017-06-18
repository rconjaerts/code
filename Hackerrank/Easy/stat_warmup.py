'''
Problem: https://www.hackerrank.com/challenges/stat-warmup
Solved: True
'''

def calcMean(x):
    return sum(x)/len(x)

def calcMedian(x):
    x.sort()
    if len(x)%2 == 0:
        return (x[int(len(x)/2)-1]+x[int(len(x)/2)])/2
    else:
        return x[floor(len(x)/2)+1]
    
def calcMode(x):
    highest = [x[0]]
    d = {}
    for n in x:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    
    for n in d:
        if d[n] > d[highest[0]]:
            highest = [n]
        elif d[n] == d[highest[0]]:
            highest.append(n)
    
    if len(highest) == 1:
        return highest[0]
    else:
        return min(highest)
    
def calcStDev(pop, mean):
    return round((sum([(x-mean)**2 for x in pop])/len(pop))**0.5, 1)

n = input().strip()
numbers = [int(x) for x in input().strip().split(' ')]

mean = calcMean(numbers)
print(mean)
print(calcMedian(numbers))
print(calcMode(numbers))
stdev = calcStDev(numbers, mean)
print(stdev)
print(str(round(mean-(1.96*(stdev/(len(numbers)**0.5))), 1))+' '+str(round(mean+(1.96*(stdev/(len(numbers)**0.5))), 1)))