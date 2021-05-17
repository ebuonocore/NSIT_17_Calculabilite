# -*- coding: utf-8 -*-
"""
Créé le 30/09/20
Dessine des carrés imbriqués en impératif

@author: Eric Buonocore
"""
from turtle import *
import math
# importation de la bibliothèque turtle

# Phase d'initialisation
a = 200 #Taille du côté d'origine
n = 5 # Profondeur maximale
c = math.sqrt(2) # Coefficient de réduction à chaque étape

clearscreen()
up()
goto(-a,a)
pensize(2)
down() # Abaisse le crayon pour pouvoir laisser une trace
speed(0)


#Corps du programme
# Descente
for i in range(n):
    forward (a/(c**i))
    right(45)
# Annule le dernier virage en trop
left(45)

for i in range(n-1, -1, -1):
    forward(a/(c**(i))) # termine le demi-segment entamé
    # Se présente dans le bon sens pour finir les 3 derniers côtés du carré
    right(90)
    for r in range (3):
        forward (2*a/(c**i))
        right(90)
    left(45)
    
exitonclick()
# Ferme la fenêtre générée par turtle
mainloop()

