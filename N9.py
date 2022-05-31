# Write a Python Program to print r*c matrix and also print its 1D array .
import numpy as np
r,c=map(int,input().split(" "))
list=eval(input(f'Enter {r*c} elements;'))
a=np.array(list,dtype=int)
a=a.reshape([r,c])
print(a)
print(a.flatten())
