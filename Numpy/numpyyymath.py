import numpy as np
#Mathematics in array 
a = np.array([1,2,3,4])
print(a)
print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)
b = np.array([1,0,1,0])
print(a + b)
print(a ** 2)
print(np.cos(a))

#linear algebra
a = np.ones((2,3))
print(a)

b = np.full((3,2), 2)
print(b)

print(np.matmul(a,b))

#find the determinant 
c= np.identity(3)
print(np.linalg.det(c))