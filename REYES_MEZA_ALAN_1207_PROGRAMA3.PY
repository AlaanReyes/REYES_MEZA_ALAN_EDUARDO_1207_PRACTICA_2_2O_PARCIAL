print("Welcome to PRACTICA 2 2NDO PARCIAL!")# Mensaje de bienvenida al usuario
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Pedir al usuario que ingrese un número entero positivo
numero = int(input("Introduce un entero positivo: "))

if numero < 0:
    print("Por favor, introduce un número entero positivo.")
else:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}.")
