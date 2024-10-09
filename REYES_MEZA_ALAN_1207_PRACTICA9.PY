print("Welcome to PRACTICA 2 2NDO PARCIAL!")# Mensaje de bienvenida al usuario
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO


def sumar(lista):
    """
    suma todos los numeros de una lista.
    """
    return sum(lista)

def multiplicacion(lista):
    """
    multiplica todos los numeros de una lista.
    """
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

if __name__ == "__main__":
    # solicita al usuario que ingrese una lista de numeros
    entrada = input("ingrese numeros separados por comas: ")
    
    # convierte la entrada en una lista de numeros
    numeros = [float(num) for num in entrada.split(",")]
    
    # calcula la suma y la multiplicacion
    suma = sumar(numeros)
    producto = multiplicacion(numeros)
    
    # muestra los resultados
    print(f"la suma de los numeros es: {suma}")
    print(f"la multiplicacion de los numeros es: {producto}")
