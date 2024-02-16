import numpy as np



#The basics 
a = np.array([1,2,3])
print(a)

b = np.array([[2.0,3.0,4.0],
              [6.0,7.0,8.0]])
print(b)

#get dimension 
print(a.ndim)
print(b.ndim)


#get shape 
print(a.shape)
print(b.shape)

#get type
print(a.dtype)
print(b.dtype)

#get size
print(a.size)
print(b.size)

#itemsize
print(a.itemsize)
print(b.itemsize)

#get total size
print(a.nbytes)