texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
texto_modificado = texto.split("&")
for i,j in enumerate(texto_modificado):
    if i == 2:
        print("-",j.capitalize().replace("-","")+".")
    if i!=0:
        print("-",j.capitalize()+".")
    else:
        print(j.capitalize()+"...")