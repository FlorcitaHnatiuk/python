grupo = {"Miguel", "Blanca", "Mario", "Andrés"}
grupo.update(['Ana', 'Ramón', 'Marta', 'Eric', 'David'])
grupo

grupo.discard('Mario')
grupo.discard('Miguel')
grupo.discard('Esteban')

# ejercicio 2
grupo = {'Miguel', 'Blanca', 'Mario', 'Andres'}
nuevos_usuarios = ['Ana', 'Ramón', 'Marta', 'Eric', 'David']
eliminados = ['Mario', 'Miguel', 'Esteban']

grupo.update(nuevos_usuarios)

for elemento in eliminados:
    grupo.discard(elemento)

print(grupo)

# ejercicio 3
animales = {"elefante": ""}
animales.update({'perro': 'Bobby', 'tigre':'Peepe', 'mono': 'Homero'})
animales['elefante'] = 'Trompis'
animales['delfin'] = 'Manolo'