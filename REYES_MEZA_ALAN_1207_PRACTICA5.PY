print("Welcome to PRACTICA 2 2NDO PARCIAL!")# Mensaje de bienvenida al usuario
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

import math

def calcular_area_circulo(radio):
    """
    calcula el area de un circulo dado su radio
    """
    area = math.pi * (radio ** 2)
    return area

def calcular_volumen_cilindro(radio, altura):
    """
    calcula el volumen de un cilindro dado su radio y altura
     """
    area_base = calcular_area_circulo(radio)  # utiliza la funcion para calcular el area del circulo
    volumen = area_base * altura
    return volumen

if __name__ == "__main__":
    try:
        # solicita al usuario el radio del circulo
        radio = float(input("ingrese el radio del circulo: "))
        
        # calcula y muestra el area del circulo
        area_circulo = calcular_area_circulo(radio)
        print(f"el area del circulo es: {area_circulo:.2f}")

        # solicita al usuario la altura del cilindro
        altura = float(input("ingrese la altura del cilindro: "))
        
        # calcula y muestra el volumen del cilindro
        volumen_cilindro = calcular_volumen_cilindro(radio, altura)
        print(f"el volumen del cilindro es: {volumen_cilindro:.2f}")
    
    except ValueError:
        # maneja el caso en que el usuario ingresa un valor no valido
        print("por favor, ingrese un numero valido.")

