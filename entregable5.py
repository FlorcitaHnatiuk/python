# ejercicio 1
def area_rectangulo(base, altura):
  return base * altura

print("El area del rectángulo es de: ")
print(area_rectangulo(10, 15))

# ejercicio 2
import math
def area_circulo(radio):
    area = math.pi*radio**2
    return print("El area del circulo es de %.3f" % area)

area_circulo(5)

# ejercicio 3
def relacion(num1, num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    return 0

print(relacion(5, 10), relacion(10, 5), relacion(5, 5))

# ejercicio 4
def recortar(num, limite_inferior, limite_superior):
    return max(min(num, limite_superior), limite_inferior)

recortar(15, 0, 10)

# ejercicio 5
numeros = [-4, 3, 6, 12, -34, 47, 100, -87, 52]

def separar(*args):
    lista = sorted(args)
    pares = []
    impares = []
    for arg in lista:
        if arg % 2 == 0:
            pares.append(arg)
        else:
            impares.append(arg)
    return pares, impares

pares, impares = separar(*numeros)
print(pares)
print(impares)