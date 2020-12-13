def main():
    a=[1,2,3,4,5,10,7,9,11]
    n=9
    for i in range(0,n):
        if a[i]%2==0:
            print(a[i])
    for i in range(0,n):
        if (a[n-1-i])%2!=0:
            print(a[n-1-i])
main()
