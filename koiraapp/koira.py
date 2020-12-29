import random
from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk,Image
import requests
from bs4 import BeautifulSoup

def getdata(osoite):

    koiralista = []

    kuvalista = []
    
    URL = osoite

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    nimet = soup.find_all('a', class_='list-item-title')

    kuvat = soup.find_all('img', class_='list-item-breed-img')

    for laji in nimet:
        koiralista.append(list(laji)[0])

    for laji in kuvat:
        kuvalista.append(laji.get('src'))   

    return koiralista, kuvalista

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

def generaterandomitem(data: list):
    uusi_lista = []
    lista = data

    uusi_lista.append(random.choice(lista))

    return uusi_lista

class generatewindow:

    def __init__(self, master):
        self.master = master

        master.title("Dog app")
        self.img = ImageTk.PhotoImage(
            Image.open((kuva(generaterandomitem(getdata("https://dogtime.com/dog-breeds/profiles")[1]))[0])))
        self.btn = tk.Button(self.master, image=self.img, borderwidth=0, highlightthickness=0, command=self.clicked)
        self.btn.pack()

    def clicked(self):
        self.btn.destroy()
        self.img = ImageTk.PhotoImage(
            Image.open((kuva(generaterandomitem(getdata("https://dogtime.com/dog-breeds/profiles")[1]))[0])))
        self.btn = tk.Button(self.master, image=self.img, borderwidth=0, highlightthickness=0, command=self.clicked)
        self.btn.pack()


window = Tk()
my_gui = generatewindow(window)
window.mainloop()