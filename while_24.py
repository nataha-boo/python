n=int(input())
x=False
f1=1
f2=1
for k in range(0,n+1):
    fk=f1+f2
    f2=f1
    f1=fk
    if(n==fk):
        x=True
print(x)
