import random


def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


# EJERCICIO A
print("EJERCICIO A")

while True:
    numero_aleatorio = random.randint(1, 100)

    if es_primo(numero_aleatorio):
        print("Numero primo aleatorio:", numero_aleatorio)
        break


# EJERCICIO B
print("\nEJERCICIO B")

try:
    n = int(input("Ingrese un valor N: "))

    print("Numeros primos hasta", n, ":")

    for numero in range(2, n + 1):
        if es_primo(numero):
            print(numero)

except ValueError:
    print("Error: debe ingresar un numero entero.")