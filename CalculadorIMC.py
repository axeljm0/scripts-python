#      IMC clasificacion 
# Menor que 18.5              Bajo peso
# 18.5 - 24.9                 Normal
# 25.0 - 29.9                 Sobrepeso
# 30.0 - 34.9                 Obesidad I
# 35.0 - 39.9                 Obesidad II
# 40.0 - 49.9                 Obesidad III
# Mayor que 50.0              Obesidad IV  
#

Altura=float(input("Introduce tu altura:"))
Peso=float(input("Introduce tu peso en KG:"))
IMC= round(Peso/(Altura**2))
print("Tu IMC es:",IMC)

if IMC < 18.5:
    print("Tienes bajo peso")
elif IMC<= 18.5:
    print("Tu peso es normal")
elif IMC <= 24.9:
    print("Tienes sobrepeso")
elif IMC <= 34.2:
    print("Tienes obesidad I")
elif IMC >= 39.9:
    print("Tienes obesidad II")

     
    

    

    
    

 