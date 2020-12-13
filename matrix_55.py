def main():
    a=[[1,2,3,4],[5,6,7,8],[3,5,7,9],[4,5,8,2]]
    m=4
    n=4
    p=m//2
    t=0
    for i in range(p,m):
        for j in range(0,n):
            print(a[i][j],end=' ')
        print()
    for i in range(0,m):
        if i<p:
            for j in range(0,n):
                t=a[i+p][j]
                a[i+p][j]=a[i][j]
                a[i][j]=t
                print(a[i+p][j],end=' ')
            print()
            
main()
