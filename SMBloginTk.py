#!/usr/bin/env python3

import tkinter
import subprocess
#import configparser
from tkinter.messagebox import *
from tkinter import *


#cfg = configparser.configParser()
#cfg.read("smb.cfg")


fenetre = Tk()


def Montage():

    pass



# Saisie login et password

auth = Label(fenetre, text="Login ")
auth.grid(row = 1, column = 1, padx = 5, pady = 5)

Login = StringVar()
Login.set("mon_login")
Entree = Entry(fenetre, textvariable = Login, bg = 'bisque', fg = 'black')
Entree.focus_set()
Entree.grid(row = 1, column = 2, padx = 5, pady = 5)

mdp = Label(fenetre, text="Password ")
mdp.grid(row = 2, column = 1, padx = 5, pady = 5)

Password = StringVar()
Entree = Entry(fenetre, textvariable = Password, show ='*', bg = 'bisque', fg = 'black')
Entree.focus_set()
Entree.grid(row = 2, column = 2, padx = 5, pady = 5)


# Bouton valider et quitter

Bouton = Button(fenetre, text= 'Valider', command = Montage)
Bouton.grid(row = 3, column = 1, padx = 5, pady = 5)

Bouton = Button(fenetre, text = 'Quitter', command = fenetre.destroy)
Bouton.grid(row = 3, column = 2, padx = 5, pady = 5)


fenetre.mainloop()



