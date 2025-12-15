# Crear una lista
lista = [1, 2, 3, 4]
print('Lista original:', lista) # Imprime: [1, 2, 3, 4]
# Obtener el iterador de la lista
iterador = iter(lista)

# Usar el iterador para obtener elementos
print(next(iterador))  # Imprime: 1
print(next(iterador))  # Imprime: 2
print(next(iterador))  # Imprime: 3
print(next(iterador))  # Imprime: 4


# Intentar obtener otro elemento después de finalizar la iteración
##print(next(iterador))  # Esto generará una excepción StopIteration


#--- 
text="hola"
var_text=iter(text)
print(next(var_text))  # Imprime: h
print(next(var_text))  # Imprime: o    
print(next(var_text))  # Imprime: l
print(next(var_text))  # Imprime: a
##print(next(var_text))  # Esto generará una excepción StopIteration

#--- Uso de un bucle for para iterar sobre una cadena
for char in text:
    print(char) # Imprime cada carácter en una línea separada




# Crear un iterador para números impares hasta 10
limite = 10
iterador_impares = iter(range(1, limite + 1, 2))

# Iterar a través de los números impares
for numero in iterador_impares:
    print(numero)