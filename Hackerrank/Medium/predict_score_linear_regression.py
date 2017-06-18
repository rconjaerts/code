'''
Problem: https://www.hackerrank.com/challenges/correlation-and-regression-lines-8
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
    

def calcSlope(pop1, mean1, pop2, mean2):        
    coeff = calcKPCoefficient(pop1, mean1, pop2, mean2)
    st_dev_pop1 = calcStDev(pop1, mean1)
    st_dev_pop2 = calcStDev(pop2, mean2)
    
    return coeff*(st_dev_pop2/st_dev_pop1)

def calcIntercept(slope, mean1, mean2):
    return mean2-(slope*mean1)
    
def predictScore(phy_score):
    # Problem with fixed input
    res_phy = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
    res_hist = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
    
    mean_phy = calcMean(res_phy)
    mean_hist = calcMean(res_hist)
    slope = calcSlope(res_phy, mean_phy, res_hist, mean_hist)
    intercept = calcIntercept(slope, mean_phy, mean_hist)
    
    return round(slope*phy_score+intercept, 1)

print(predictScore(10))