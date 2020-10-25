n=int(input())
a=[]
kol=0
for i in range(n):
    a.append(int(input()))
for i in range(1,n):
    if(a[i-1]<a[i]):
        kol+=1
        print(a[i-1],"- меньше числа справа")
print("Количество таких чисел - ", kol)
