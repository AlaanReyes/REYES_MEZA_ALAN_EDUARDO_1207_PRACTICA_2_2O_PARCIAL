print("Welcome to PRACTICA 2 2NDO PARCIAL!")# Mensaje de bienvenida al usuario
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def distancia_dirigida(x1, y1, x2, y2):
    """
    calcula la distancia dirigida entre dos puntos.
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if __name__ == "__main__":
    # solicita las coordenadas de los dos puntos
    x1 = float(input("ingrese la coordenada x del primer punto: "))
    y1 = float(input("ingrese la coordenada y del primer punto: "))
    x2 = float(input("ingrese la coordenada x del segundo punto: "))
    y2 = float(input("ingrese la coordenada y del segundo punto: "))
    
    # calcula la distancia dirigida
    distancia = distancia_dirigida(x1, y1, x2, y2)
    
    # muestra el resultado
    print(f"La distancia dirigida entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {distancia:.2f}")
