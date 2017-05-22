'''
Problem: https://www.hackerrank.com/challenges/correlation-and-regression-lines-6
Solved: True
'''

def calcMean(x):
    return sum(x)/len(x)

def calculateKPCoefficient():
    # Problem with fixed input
    res_phy = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
    res_hist = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
    
    mean_phy = calcMean(res_phy)
    mean_hist = calcMean(res_hist)
    
    diff_phy = [x-mean_phy for x in res_phy]
    diff_hist = [x-mean_hist for x in res_hist]
    
    numerator = sum(x*y for x, y in zip(diff_phy, diff_hist))
    denominator = (sum(x**2 for x in diff_phy))**0.5 * (sum(x**2 for x in diff_hist))**0.5
    return round(numerator/denominator, 3)
    
print(calculateKPCoefficient())