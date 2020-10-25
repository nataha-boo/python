import math
x=float(input())
n=int(input())
summa=1
a=1
if(x!=0):
    y=x**2
    for i in range (1,n):
        a=-((a*y)/((2*i-1)*2*i))
        summa+=a
print(summa)
