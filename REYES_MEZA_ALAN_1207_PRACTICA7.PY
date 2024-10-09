print("Welcome to PRACTICA 2 2NDO PARCIAL!")# Mensaje de bienvenida al usuario
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def longitud_ultima_palabra(texto):
    """
    regresa la longitud de la ultima palabra en un string..
    """
    # eliminar espacios al principio y al final, y dividir el texto en palabras
    palabras = texto.strip().split()
    
    # verificar si hay palabras en el texto
    if palabras:
        return len(palabras[-1])  # devolver la longitud de la ultima palabra
    else:
        return 0  # si no hay palabras, devolver 0

if __name__ == "__main__":
    # solicita al usuario que ingrese un texto
    texto = input("ingrese un texto: ")
    
    # calcula la longitud de la ultima palabra
    longitud = longitud_ultima_palabra(texto)
    
    # muestra la longitud de la ultima palabra
    print(f"la longitud de la ultima palabra es: {longitud}")
