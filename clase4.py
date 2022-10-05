#ejercicio 1
edad = int(input("ingresa tu edad\n"))
if (edad >= 18):
    print("Podes tomar alcohol")
else:
    print("No podes tomar alcohol")

# ejercicio 2
nombre = input("como te llamas?\n")
preferencia = input("Cual preferis? Marvel o Capcom?")
if((nombre[0]<="M" and preferencia == "Marvel") or (nombre[0] >= "N" and preferencia == "Capcom")):
    print("Sos del grupo A")
else:
    print("Sos del grupo B")

#ejercicio 3
comando = "salir"
if comando == "entrar":
    print("Bienvenido")
elif comando == "saludo":
    print("Hola como estas?")
elif comando == "salir":
    print("chau")
else:
    print("no reconozco ese comando")

#ejercicio 4
nota = int(input("cual es tu nota?\n"))
if nota >= 9:
    print("Excelente")
elif nota >= 7 and nota < 9:
    print("Muy bien")
elif nota == 6:
    print("Bien")
elif nota >= 4 and nota <= 5:
    print("regular")
else:
    print("insuficiente")