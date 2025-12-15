
# Manejo de múltiples excepciones
while True: 
    try:
        numero = int(input("Ingrese un numero entero: "))
        resultado = 100 / numero
        print("El resultado de la division es :", resultado)
        break
    except ZeroDivisionError as e:
        print("Error: No se puede dividir por cero. Intente de nuevo.")
        print("Detalles del error:", e)
    except ValueError as e:
        print("Error: Entrada invalida. Por favor, ingrese un numero entero.")
        print("Detalles del error:", e)