def saludar(name,apellido=" "):
    print("hola ",name, apellido)

saludar("camilo","diaz")
saludar("carolina")


def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def dividir(a,b):
    return a/b

def multiplicar(a,b):
    return a*b

def calculadora():
    while True:
        print("Seleccione una opcion: ")
        print("1. Sumar")
        print("2. Restar")
        print("3. Dividir")
        print("4. Multiplicar")
        print("5. Salir")
        opcion = input("Ingrese la opcion 1,2,3,4,5: ")
        if opcion=="5":
            print("Saliendo de la calculadora")
            break
        if opcion in ['1','2','3','4']:
            num1=float(input("Ingrese el primer numero :"))
            num2=float(input("Ingrese el segundo  numero :"))
            if opcion =="1":
                print("La suma es :",sumar(num1,num2))
            elif opcion =="2":
                 print("La resta es :",restar(num1,num2))
            elif opcion =="3":
                 print("La division es :",dividir(num1,num2))
            elif opcion =="4":
                 print("La multiplicacion es :",multiplicar(num1,num2))
        else:
            print("Opcion invalida, por favor intente de nuevo.")
        
calculadora()




