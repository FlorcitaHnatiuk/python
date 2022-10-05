# ejercicio 1
nota_1 = int(input("Cual fue la primer nota? \n"))*0.4
nota_2 = int(input("Cual fue la segunda nota? \n"))*0.6
total = nota_1+nota_2
print(f"Tu nota final es {total}")

# ejercicio 2
cadena_1 = "moderno"
cadena_2 = "Python"
cadena_3 = "es un lenguaje"
cadena_4 = "de programación"
espacio = " "
mi_frase = cadena_2 + espacio + cadena_3 + espacio + cadena_1 + espacio + cadena_4
print(mi_frase)

# ejercicio 3
# Para evitar girar a mano la frase, hice la siguiente función
str="Emmanuel Sanabria, 10, matemáticas"
# print(len(str))
sliced_str=str[::-1]
# print(sliced_str)
# Esta es la función del ejercicio a realizar
cadena = "sacitámetam ,01 ,airbanaS leunammE"
cadena_girada = cadena[::-1]
# print(cadena_girada)
nombre_alumno = cadena_girada [0:17]
nota = cadena_girada[19:21]
materia = cadena_girada [23:34]
devolucion = f"El alumno {nombre_alumno} se sacó un {nota} en {materia}"
devolucion