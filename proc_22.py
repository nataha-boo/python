def Calc(A,B,Op):
    if Op==1:
        return A-B
    elif Op==2:
        return A*B
    elif Op==3:
        return A/B
    else:
        return A+B


A=float(input("А: "))
B=float(input("B: "))
N1=int(input("N1: "))
N2=int(input("N2: "))
N3=int(input("N3: "))

print(Calc(A,B,N1))
print(Calc(A,B,N2))
print(Calc(A,B,N3))
