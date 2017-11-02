import numpy as np 

m1 = np.array([[1,1],[1,1]])
m2 = np.array([[2,2],[2,2]])

res = np.sum(np.dot(m1, m2))
print(res)