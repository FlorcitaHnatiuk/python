# ejercicio 1
f = open('/content/ejemplo_escritura.txt', 'w')

f.write('adios a todos')

f.close()

# ejercicio 2
f = open('/content/ejemplo_escritura.txt', 'w')

texto = input('Ingrese un texto')

f.write(texto)

f.close()

# ejercicio 3
f = open('/content/ejemplo_escritura.txt', 'a')

dni = 1234

f.write(str(dni))

f.close()

# ejercicio 4
chat_string = ''
while True:
    chat = input('Escriba un mensaje, 0 para salir \n')
    if chat == '0':
        chat = ''
        break
    chat_string += chat + '\n'

chat_file = open('/content/ejemplo_lecturaa.txt', 'a')
chat_file.write(chat_string)
chat_file.close()

# ejercicio 5
while True:
    chat_file = open('/content/chat.txt', 'a')

    chat = input('Escriba un mensaje, 0 para salir \n')
    if chat == '0':
        chat = ''
        break
    chat_file.write(chat)

    chat_file.close()

# ejercicio 6
# Utilizando read
ejemplo_lectura = open('/content/ejemplo_lectura.txt', 'r')
print(ejemplo_lectura.read())
ejemplo_lectura.close()

# ejercicio 7
# Utilizando readline
ejemplo_lectura = open('/content/ejemplo_lectura.txt', 'r')
print(ejemplo_lectura.readline())
ejemplo_lectura.close()

# ejercicio 8
# Utilizando readlines
ejemplo_lectura = open('/content/ejemplo_lectura.txt', 'r')

for linea in ejemplo_lectura.readlines():
    print(linea)
ejemplo_lectura.close()

# ejercicio 9
# Utilizando seek
ejemplo_lectura = open('/content/ejemplo_lectura.txt', 'r')
ejemplo_lectura.seek(30) #[6:]
print(ejemplo_lectura.read())
ejemplo_lectura.close()

# ejercicio 10
opcion = int(input('Digite 1 para iniciar sesion o 2 para registrarse: '))

if (opcion == 1):
  print('Iniciar Sesion')

  username = input('Usuario: ')
  pwd = input('Contraseña: ')

  file = open('/content/usuarios.txt', 'r')
  for linea in file.readlines():
    print(linea)
    data = linea.split(',')

    if(data[0] == username and data[1] == pwd):
      print(f'Bienvenido a Facebook :D {data[2]} {data[3]}')
      file.close()
      break
    else:
      print('Usuario o contraseña incorrectos')

elif (opcion == 2):
  print('Registro')
  username = input('Usuario: ')
  pwd = input('Contraseña: ')
  nombre = input('Nombre: ')
  apellido = input('Apellido: ')

  f = open('/content/usuarios.txt', 'a')

  # username,password,nombre,apellido
  f.write(f'{username},{pwd},{nombre},{apellido}\n')

  f.close()


else:
  print('Opcion no valida')

# ejercicio 11
nombre = input('Como se llama tu mascota: ')
edad = input('Cuantos años tiene?: ')
tipo_animal = input('Que tipo de animal es?: ')

f = open('/content/desafio1.txt', 'a')

f.write(f'Mi mascota se llama {nombre}, tiene {edad} años y es {tipo_animal} \n')
f.close()

# ejercicio 12
# Utilicemos dump para cargar el JSON de ejemplo en un archivo
dict_ejemplo = { 
    "cliente": {
        "id": 2020, 
        "nombre": "Maria Aparecida" 
    },
    "pagos": [  
        {  
            "id": 123,   
            "descripcion": "Compra del libro Cangaceiro JavaScript",    
            "valor": 50.5   
        },   
        {    
            "id": 124,    
            "descripcion": "Mensualidad escolar",    
            "valor": 1500   
        }  
    ]
}



with open('/content/ejemplo_json.json', 'w') as file: # file = open()
    #json.dump(dict_ejemplo, file) # file.write()
# Utilicemos load para leer el ejemplo
    with open('/content/ejemplo_json.json', 'r') as file:
    #data = json.load(file) # file.read()
        print(data)

# ejercicio 13
opcion = int(input('Digite un 1 para iniciar sesion o un 2 para registrarse: '))
new_data = {
    'usuarios': []
}
#{usuarios: [lista]}
#Clave : valor

if(opcion == 1):
    print('INICIAR SESION\n')
    username = input('Username: ')
    pwd = input('Contraseña: ')
    with open('/content/usuarios.json', 'r') as file:
        #data = json.load(file)
        for user in data['usuarios']:
            if(user['username'] == username and user['pwd'] == pwd):
                print(f'Bienvenido a Fakebook :D {username}')
                print('En que estas pensando...')
                break
        else:
            print('Usuario no encontrado')
elif(opcion == 2):
    print('REGISTRO\n')

    newdata = {
        'username': input('Username: '),
        'pwd' : input('Contraseña: '),
        'name' : input('Nombre: '),
        'lastName' : input('Apellido: ')
    }
    #file = open('/content/usuarios.json', 'r')
    with open('/content/usuarios.json', 'r') as file:
        #data = json.load(file)
        data['usuarios'].append(newdata)

    with open('/content/usuarios.json', 'w') as file:
        #json.dump(data,file)
        print('Registro Exitoso!')
else:
    print('Opcion no valida')