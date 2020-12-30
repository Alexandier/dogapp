from getdata import *

def kuva(data: list):

    lista = data
    uusi_lista = []

    määrä = len(lista)

    for i in range(määrä):
        response = requests.get(lista[i])

        file = open("image{}.png".format(i), "wb")
        file.write(response.content)
        file.close()

        uusi_lista.append("image{}.png".format(i))

    return uusi_lista