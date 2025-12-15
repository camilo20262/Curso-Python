


def suma_naturales(n):
    if n == 0:
        return 0
    else:
        return n + suma_naturales(n - 1)

print(suma_naturales(5))  # Salida: 15 (5 + 4 + 3 + 2 + 1 + 0)

print(suma_naturales(4)) # Salida: 10 (4 + 3 + 2 + 1 + 0)