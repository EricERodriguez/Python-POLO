import sys

try:
    numero1 = int(input("Ingrese numero 1: "))
    numero2 = int(input("Ingrese numero 2: "))
except ValueError:
    print("Error. Valor no valido")
    sys.exit(1)

try:
    resultado = numero1 / numero2
except ValueError:
    print("Error. Valor no valido")
    sys.exit(1)
else:
    print("La division salio como se esperaba.")

numero1 = int(input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero 2: "))

resultado = numero1 / numero2

print(f"El resultado de dividir {numero1} por  {numero2} es - {resultado}")