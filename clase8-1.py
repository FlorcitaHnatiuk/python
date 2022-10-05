from os import write

ruta = open("/content/drive/MyDrive/34635/miMascota.txt","w")
option = int(input("""
1. Agregar Mascota
2. Salir
"""))
while(option!=2):
  nombre = str(input("cual es el nombre de la mascota?\n"))
  edad = str(input("Cual es la edad del animal?\n"))
  tipo = str(input("Cual es el tipo de mascota?\n"))
  mascota = {
      "nombre":nombre,
      "edad":edad,
      "tipo":tipo,
  }
  ruta.write(f'{mascota["nombre"]}, {mascota["edad"]}, {mascota["tipo"]}\n')  
  option = int(input("""
    1. Agregar Mascota
    2. Salir
  """))
else:
  ruta.close()