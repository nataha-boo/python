A=float(input("Введите первый коэффициент - "))
B=float(input("Введите второй коэффициент - "))
C=float(input("Введите третий коэффициент - "))
if (A!=0):
    x1=(-B+(B*B-4*A*C)**(1/2))/(2*A)
    x2=(-B-(B*B-4*A*C)**(1/2))/(2*A)
    if (x1<x2):
        print("Первый корень = ",x1)
        print("Второй корень = ",x2)
    else:
        print("Первый корень = ",x2)
        print("Второй корень = ",x1)
