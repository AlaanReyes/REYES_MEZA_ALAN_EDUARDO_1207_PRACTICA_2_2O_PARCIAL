print("Welcome to PRACTICA 2 2NDO PARCIAL!")# Mensaje de bienvenida al usuario
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def calcular_total_factura(monto_sin_iva, porcentaje_iva=21):
    """
    Calcula el total de una factura después de aplicar el IVA.
    """
    # Calcula el total multiplicando el monto sin IVA por (1 + porcentaje de IVA / 100)
    total = monto_sin_iva * (1 + porcentaje_iva / 100)
    return total
if __name__ == "__main__":
    try:
        # Solicita al usuario que ingrese el monto sin IVA
        monto_sin_iva = float(input("Ingrese el monto sin IVA: "))
        
        # Solicita al usuario que ingrese el porcentaje de IVA
        porcentaje_iva = input("Ingrese el porcentaje de IVA (presione Enter para 21%): ")
        
        # Si el usuario no ingresa un porcentaje, se utiliza el 21%
        if porcentaje_iva == "":
            total_factura = calcular_total_factura(monto_sin_iva)
        else:
            total_factura = calcular_total_factura(monto_sin_iva, float(porcentaje_iva))
        
        # Muestra el total de la factura formateado a dos decimales
        print(f"El total de la factura es: {total_factura:.2f}")
    
    except ValueError:
        # Maneja el caso en que el usuario ingresa un valor no válido
        print("Por favor, ingrese un número válido.")

