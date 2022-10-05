# Ejemplo funcion basica
def saludar():
    print('Hola team CODER!!!')

saludar()

# Ejemplo funcion
def saludar(nombre):
    print(f'Hola {nombre}')

saludar('Maria')

# Ejemplo funcion con parametros

def saludar_con_parametro(nombre):
    print(f'Hola {nombre} del team CODER!!!')

# Equivalente a:
# print(f'Hola {nombre} del team CODER!!!')

nombre = input('Nombre: ')
saludar_con_parametro(nombre)

# ejercicio
variable_test = 10

def test():
    variable_test = 2
    return variable_test


variable_test = test()
print(f'Este es el print normal {variable_test}')

#ejercicio
def suma(valor1, valor2):
    print(valor1 + valor2)

resultado = suma(3, 2)
print(resultado)

# Ejemplo 1 Calculadora
def calculadora(num1, num2, operacion):
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == 'x':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2
    else:
        resultado = 'No se encontro la operacion'
    return resultado
print(f'{calculadora(3, 3, "+")}')

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
operacion = input("Operacion: ")

print(f'{calculadora(numero1, numero2, operacion)}')

# ejercicio
def suma(lista):
    resultado = 0
    for numero in lista:
        resultado += numero
    return resultado


print(sum([1, 2, 3]))
print(suma([1, 2, 3]))

# Ejemplo 2 Recrear la funcion sum

# sum([1, 2, 4])

def suma(lista):
    resultado = 0
    for elemento in lista:
        resultado += elemento

    return resultado

print(sum([1, 2, 4]))
print(suma([1, 2, 4]))

# ejercicio
print('TRANSACCION')
print('O:Operador\nV:Verificador\nA:Autorizador')
opcion = input('Selecione una opcion: ').upper()
if (opcion == 'O'):
  with open('/content/data_usuarios.txt','r') as datos:
    for data in datos:
      detalles = data.split('|')
      if (detalles[0] == 'operador'):
        print(f'El operador de la transaccion fue {detalles[3]}')
        break
elif (opcion == 'V'):
  with open('/content/data_usuarios.txt','r') as datos:
    for data in datos:
      print(data)
      detalles = data.split('|')
      if (detalles[0] == 'verificador'):
        print(f'El verificador de la transaccion fue {detalles[3]}')
        break
elif (opcion == 'A'):
  with open('/content/data_usuarios.txt','r') as datos:
    for data in datos:
      detalles = data.split('|')
      if (detalles[0] == 'autorizador'):
        print(f'El autorizador de la transaccion fue {detalles[3]}')
        break
else:
  print('Opcion no valida')

# else
def identificar_usuario(opcion):
  with open('/content/data_usuarios.txt','r') as datos:
    for data in datos:
      detalles = data.split('|')
      if (detalles[0] == opcion):
        return detalles

# else
print('TRANSACCION')
print('O:Operador\nV:Verificador\nA:Autorizador')
opcion = input('Selecione una opcion: ').upper()
if (opcion == 'O'):
  usuario = identificar_usuario('operador')
elif (opcion == 'V'):
  usuario = identificar_usuario('verificador')
elif (opcion == 'A'):
  usuario = identificar_usuario('autorizador')
else:
  print('Opcion no valida')

print(f'El usuario con rol de {usuario[0]} fue {usuario[3]} {usuario[4]}')