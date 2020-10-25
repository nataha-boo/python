k=int(input())
n=int(input())
a=[]
s=0
for i in range(k*n):
    a.append(int(input()))
for i in range(k*n):
    s+=a[i]
print("Сумма всех элементов = ", s)
