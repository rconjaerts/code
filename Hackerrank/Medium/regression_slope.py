'''
Problem: https://www.hackerrank.com/challenges/correlation-and-regression-lines-7
Solved: True
'''

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
    

def calcSlope():
    # Problem with fixed input
    res_phy = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
    res_hist = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
    
    mean_phy = calcMean(res_phy)
    mean_hist = calcMean(res_hist)
    
    coeff = calcKPCoefficient(res_phy, mean_phy, res_hist, mean_hist)
    st_dev_phy = calcStDev(res_phy, mean_phy)
    st_dev_hist = calcStDev(res_hist, mean_hist)
    
    return round(coeff*(st_dev_hist/st_dev_phy), 3)
    
print(calcSlope())