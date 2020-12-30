import random
from convertintophoto import *https://github.com/Alexandier/dogapp/blob/main/koiraapp/koira.py
from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk, Image

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
