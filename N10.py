#Write a Python Program to know the sum of indiviual sum of row and column.
import numpy as np
r,c=map(int,input().split(" "))
list=eval(input(f'Enter {r*c} elements;'))
a=np.array(list,dtype=int)
a=a.reshape([r,c])
print(a)
print(np.sum(a,axis=1))
print(np.sum(a,axis=0))
