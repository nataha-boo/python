def main():
    n=int(input("N: "))
    miin=0
    print("Введите",n,"целых чисел: ")
    for i in range(1,n+1):
        x=int(input())
        if x>0:
            if (miin==0) or (miin>x):
                miin=x
    print("Ответ: ",miin)
main()
