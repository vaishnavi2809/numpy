#Write a python program to know to maximum and minimum value from matrix.

import numpy as np
r,c=map(int,input("Enter row and column").split(" "))
list=eval(input())
a=np.array(list,dtype=int)
a=a.reshape([r,c])
print(a)
print(np.max(a))
print(np.min(a))
