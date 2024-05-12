# Calculadora
from numpy import *

number1=float(input("Ingrese un numero:"))
number2=float(input("Ingrese el siguiente numero:"))

eleccion=0
while eleccion != 5:
    print("""
    Indique la operacion a realizar:
    1)SUma
    2)Resta
    3)Multiplicacion
    4)Division
    5)Salir
    6)Operar nuevamente
    """)    

    eleccion = float(input())

    if eleccion == 1:
        print(" ")
        print("Resultado", number1,"+", number2,"=", number1+number2)

    if eleccion == 2:
        print(" ")
        print("resultado", number1,"-", number2, "=", number1-number2)  

    if eleccion== 3:
        print(" ")
        print("resultado", number1,"*", number2, "=", number1*number2)  

    if eleccion== 4:
        print(" ")
        print("resultado", number1,"/", number2, "=", number1/number2)  

    if eleccion == 5:
     print("adios")
     break
      
    elif eleccion== 6:
      numero3=float(input("Ingrese un numero:"))
      numero4=float(input("Ingrese el siguiete numero:"))
