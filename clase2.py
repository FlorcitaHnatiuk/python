#Ejercicio 1
lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

lista1.append(1234)
lista1.append("Hola")
lista1

#Ejercicio 2
lista2.append("Adios")
lista2.append(1234)
print(lista2)

#ejercicio 3
lista3 = lista1[:-1]
lista3

#ejercicio 4
lista4 = lista2[1:-1]
lista4

#ejercicio 5
lista5 = lista4+lista3
lista5

#ejercicio 6
tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)
tupla[-1]
len(tupla)
tupla.index(87)
tupla[-3:]
tupla[8]
tupla.count(7)

#ejercicio 7
matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

filas = len(matriz)

for fila in range(filas):
    suma = sum(matriz[fila])
    matriz[fila].append(suma)

print(matriz)