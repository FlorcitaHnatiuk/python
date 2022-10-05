#ejercicio 1
def valid_name(name):
    if(type(name) == str):
        return f"{name} es un nombre valido"
    else:
        return "Error: Solo strings"

valid_name("pepe")
valid_name(2)
valid_name(10.5)

#ejercicio 2
def valid_name(name):
    if isinstance(name,str):
        return f"{name} es un nombre valido"
    else:
        return "Error: Solo strings"