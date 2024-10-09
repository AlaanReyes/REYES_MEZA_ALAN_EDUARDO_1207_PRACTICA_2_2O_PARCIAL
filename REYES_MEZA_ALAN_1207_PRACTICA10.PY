print("Welcome to PRACTICA 2 2NDO PARCIAL!")# Mensaje de bienvenida al usuario
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO


def es_vocal(caracter):
    """
    verifica si el caracter es una vocal.
    """
    return caracter.lower() in 'aeiou'

if __name__ == "__main__":
    # solicita al usuario que ingrese un caracter
    entrada = input("ingrese un caracter: ")
    
    # verifica que la entrada sea un solo caracter
    if len(entrada) == 1:
        # verifica si es una vocal
        if es_vocal(entrada):
            print("el caracter es una vocal.")
        else:
            print("el caracter no es una vocal.")
    else:
        print("por favor, ingrese solo un caracter.")
