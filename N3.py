#Write a program to test whether none of the elements of a given numpy array is more than 100

import numpy as np
n=int(input("Enter the number of element you want to insert"))
lst=[]
f=0
for i in range(n):
    x=eval(input())
    lst.append(x)
a=np.array(lst,dtype=int)
for i in range(n):
    if a[i]<101:
        f=1
    else:
        f=0
        break
if f==1:
    print("None of the Element is greater than 100")
    print(a)
else:
    print("Element is greater than 100")
    print(a)
