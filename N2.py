# Write a Pyhton Program to know the dimension of the array in the form of tuple.
import numpy as np
r,c=map(int,input().split(" "))
list=eval(input(f'Enter {r*c} elements;'))
a=np.array(list,dtype=int)
a=a.reshape([r,c])
print(a)
print(np.shape(a))
