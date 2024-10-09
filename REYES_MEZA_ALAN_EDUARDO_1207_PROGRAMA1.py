print("Welcome to PRACTICA 2 2NDO PARCIAL!")# Mensaje de bienvenida al usuario
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO
#definir SALUDAR 
def saludar():
    print("Hey amigos!") #mensaje de saludo

while True:
    input("Presiona Enter para recibir un saludo... ") #al dar ENTER recibes un saludo
    saludar() #saludo
    continuar = input("¿Quieres un saludo mas? (si/no): ") #selecciona si quisieras otro saludo 
    if continuar.lower() != 'si': #si tu respuesta es SI te muestra otro saludo
        break #Cerrar While