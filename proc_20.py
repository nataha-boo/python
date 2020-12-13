import math

def TriangleP(a,h):
    b=math.sqrt((a/2)**2+h**2)
    return b

for i in range(1,4):
    a=int(input("Введите основание треугольника: "))
    h=int(input("Введите высоту, проведенную к этому оснванию: "))
    b=TriangleP(a,h)
    P=2*b+a
    print("Периметр равнобедренного треугольника=",P)
    
