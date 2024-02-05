import time 
print(time.ctime(0)) # convert a time expressed in seconds since epoch to a readable string
                     # epoch = when your computer thinks time began (reference point)
print(time.time())   #return current seconds since epoch 

print(time.ctime(time.time()))