# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:50:29 2019
Dessine des carrés imbriqués en impératif

@author: Eric Buonocore
"""
from turtle import *
import math
# importation de la bibliothèque turtle

def pen_style(niveau_max, niveau):
    """ Modifie la taille et la couleur du stylo en fonction du niveau max et du niveau actuel
    """
    m = math.sqrt(2)**niveau
    dim = int(10 / m)
    pensize(dim)
    r = (niveau_max- niveau)/niveau_max
    v = 0.1
    b = niveau/niveau_max
    col = (r, v, b)
    pencolor(col)


# Phase d'initialisation
a = 200 #Taille du côté d'origine
n = 2 # Profondeur maximale
c = math.sqrt(2) # Coefficient de réduction à chaque étape

colormode(1)
clearscreen()
up()
goto(-a,a)
pensize(2)
down()
speed(0)
# Abaisse le crayon pour pouvoir laisser une trace

#Corps du programme

# Descente
for i in range(n):
    pen_style(n,i)
    forward (a/(c**i))
    right(45)
# Annule le dernier virage en trop
left(45)

for i in range(n-1, -1, -1):
    pen_style(n,i)
    forward(a/(c**(i))) # termine le demi-segment entamé
    # Se présente dans le bon sens pour finir les 3 derniers côtés du carré
    right(90)
    for r in range (3):
        pen_style(n,i)
        forward (2*a/(c**i))
        right(90)
    left(45)
    
exitonclick()
# Ferme la fenêtre générée par turtle
mainloop()

