print("Welcome to PRACTICA 2 2NDO PARCIAL!")# Mensaje de bienvenida al usuario
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def es_email_valido(email):
    """
    verifica si la direccion de email es valida.
    """
    return '@' in email

if __name__ == "__main__":
    # solicita al usuario que ingrese una direccion de email
    email = input("ingrese su direccion de email: ")
    
    # verifica si la direccion de email es valida
    if es_email_valido(email):
        print("la direccion de email es valida.")
    else:
        print("la direccion de email no es valida.")
