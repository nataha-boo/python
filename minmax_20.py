def main():
    kolmiin=1
    kolmaax=1
    miin=100000000
    maax=0
    N=int(input("N: "))
    print("Введите ",N,"целых чисел:")
    for i in range(1,N+1):
        x=int(input())
        if (miin==0) or (miin>x):
            miin=x
            if miin==x:
                kolmiin+=1
            else:
                kolmiin=1
        if(maax==0) or (maax<x):
            maax=x
            if maax==x:
                kolmaax+=1
            else:
                kolmaax=1
    print("Количество минимальных элементов =",kolmiin)
    print("Количество максимальных элементов =",kolmaax)
    print("Общее количество экстремальных элементов =",kolmiin+kolmaax)
main()
          
        
