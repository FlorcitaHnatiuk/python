# ejercicio 1
n1 = int(input("Ingresa un numero\n"))
n2= int(input("Ingresa otro numero\n"))
total = 0
while True:
    option = str(input("Suma(s), Resta(r), Multiplicar(m) o Finalizar(f)"))
    if option == "s":
        print(f"La suma es {n1+n2}")
    elif option == "r":
        print(f"La resta es {n1-n2}")
    elif option == "m":
        print(f"La multiplicacion es {n1*n2}")
    elif option not in("s", "r", "m", "f"):
        print("No es válido")
    elif option == "f":
        print(f"Programa finalizado, el total es {total}")
        break

# ejercicio 2
numero = int(input("Ingresá un número: "))
while numero >= 0:
    if numero % 2 == 0:
        print("Tu número es par. Por favor, ingresá un número nuevamente.")
        numero = int(input("Ingresá un número: "))
    elif numero % 2 != 0:
        print("Este número es correcto!")
        break

# ejercicio 3
suma = 0
numeros = int(input("Cuantos números querés?"))
for x in range(numeros):
    suma += float(input("Introducí un número: "))
print(f"Introduciste ", numeros, "números, que dan un total de ", suma, "La media es de", suma/numeros)

# ejercicio 4
numeros = [1, 3, 6, 9]
while (True):
    numero = int(input("Escribe un número entre 0 y 9: "))
    if numero >= 0 and numero <= 9:
        break
    if numero in numeros:
        print("El numero ", numero, "esta en la lista.")
    else:
        print("Ese número no esta en la lista")

# ejercicio 5
print(list(range(0,11)))
print(list(range(-10,1)))
print(list(range(0,21,2)))
print(list(range(-19,0,2)))
print(list(range(0,51,5)))

# ejercicio 6
lista_1 = ["h", "o", "l", "a", " ", "m", "u", "n", "d", "o"]
lista_2 = ["h", "o", "l", "a", " ", "l", "u", "n", "a"]
lista_3 = []
for letra in lista_1:
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)
print(lista_3)