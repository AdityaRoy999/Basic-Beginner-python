import numpy as np 
stats = np.array([[1,2,3],
                  [4,5,6]])
print(stats)
print(np.min(stats,axis=1))
print(np.max(stats))
print(np.sum(stats)) # give sum of all the elements in the matrix
print(np.sum(stats,axis = 0)) 

