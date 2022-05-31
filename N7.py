# Write a Python Program to calculate the sum of diagonal elements of matrix.
import numpy as np
r,c=map(int,input("Enter row and column for Square matix").split(" "))
list=eval(input(f'Enter {r*c} elements in list' ))
a=np.array(list,dtype=int)
a=a.reshape([r,c])
print(a)
d=np.diagonal(a)
print(sum(d))
