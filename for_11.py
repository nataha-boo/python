N=int(input())
a=[]
s=N*N
for i in range (1,N+1):
    s=s+((N+i)*(N+i))
print('Сумма =',s)
