def main():
    a=[[1,2,3,4],[5,6,7,8],[9,3,5,6],[7,5,9,2]]
    m=4
    n=4
    for i in range(0,m):
        for j in range(0,n):
            print(a[m-1-i][j],end=' ')
        print()
main()
