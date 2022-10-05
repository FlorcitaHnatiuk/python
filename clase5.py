# ejercicio 1
num = 5
while num > 0:
    print(f"{num}")
    num -= 1
    print("Terminó el conteo")

# ejercicio 2
chance = 1
while chance <= 3:
    txt = input("Escribi 'SI':")
    if txt == "SI":
        print("Ok, lo conseguiste en el intento n° ", chance)
        break
    chance += 1
else:
    print("No tenés mas intentos")

# ejercicio 3
ingresoNum = int(input("Ingresá un número"))
n2 = 5
while n2 < 10:
    n2 -= 1
    if n2 == 2:
        print("Ahora que n2 vale 2, salimos")
        break
    print("n2 vale ", n2)

# ejercicio 4
c = -3
while True:
    c += 1
    if c == 2:
        print("ahora que c vale 2 salimos")
        break
    print("c vale ", c)

# ejercicio 5
n = 0
while n < 10:
    n += 1
    if n == 2:
        print("continuemos iterando")
        continue
    print("n vale ", n)

# ejercicio 6
n = 0
while n < 10:
    n += 1
    if n == 2:
        pass
    print("n vale ", n)

# ejercicio 7
c = -3
while c < 10:
    c += 1
    if c == 2:
        pass
    print("c vale ", c)

# ejercicio 8
lista = [1, 2, 3, 4, 5]
for valor in lista: 
    print("Soy un item en la lista y valgo ", valor)
    valor *= 5
    print("Soy un item en la lista y ahora valgo ", valor)

# ejercicio 9
index = 0
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    numeros[index] *= 5
    index += 1
print(numeros)

# ejercicio 10
lista = [66, -3, 35, 96]
for index, numero in enumerate(lista):
    print(f"INDICE: {index}")
    print(f"NUMERO: {numero}\n\n")
    print(f"-------->{lista[index]}\n\n<--------------")

#ejercicio 11
texto = "Hola mundo Python"
for letra in texto:
    print(letra)

# ejercicio 12
for numero in range(10):
    if numero == 2:
        continue
    elif numero == 8:
        break
    print("numero vale ", numero)
else:
    print("termine de iterar y el numero final es ", numero)

# ejercicio 13
paises = ['Canada', 'USA', 'Mexico', 'Australia', 'Argentina', 'China','India']
for pais in paises:
    print("Soy de ", pais)

