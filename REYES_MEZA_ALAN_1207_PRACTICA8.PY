print("Welcome to PRACTICA 2 2NDO PARCIAL!")# Mensaje de bienvenida al usuario
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def mayor_de_tres(num1, num2, num3):
    """
    devuelve el mayor de tres numeros.
    """
    return max(num1, num2, num3)

if __name__ == "__main__":
    try:
        # solicita al usuario que ingrese tres numeros
        numero1 = float(input("ingrese el primer numero: "))
        numero2 = float(input("ingrese el segundo numero: "))
        numero3 = float(input("ingrese el tercer numero: "))
        
        # calcula el mayor de los tres numeros
        mayor = mayor_de_tres(numero1, numero2, numero3)
        
        # muestra el resultado sin decimales si es un entero
        if mayor.is_integer():
            print(f"el mayor de los tres numeros es: {int(mayor)}")
        else:
            print(f"el mayor de los tres numeros es: {mayor}")
    
    except ValueError:
        # maneja el caso en que el usuario ingresa un valor no valido
        print("por favor, ingrese un numero valido.")

