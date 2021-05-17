# -*- coding: utf-8 -*-
"""
Creéé le 03/09/20
Dessine des carrés imbriqués en impératif

@author: Eric Buonocore
"""
from turtle import *
import math
# importation de la bibliothèque turtle

def pen_rstyle(cote_carre):
    """ Modifie la taile et la couleur du stylo en fonction de la dimension du carré
    """
    dim = cote_carre // 20
    pensize(dim)
    r = min(1, abs(200- cote_carre)/200)
    v = 0.1
    b = min(1, cote_carre/200)
    col = (r, v, b)
    pencolor(col)
    
def trace_carre_rec(cote_carre, nb_carres):
    """ Trace un carré de côté 'cote_carre'
        Ce carré contient 'nb_carres' imbriqués
    """
    pen_rstyle(cote_carre)
    c = math.sqrt(2) # Coefficient de réduction à chaque étape
    # Commence par tracer le premier demi_segment
    forward(cote_carre/2)
    # Si il y un nombre positif de carrés imbriqués à dessiner
    if nb_carres > 0:
        # Alors, on se place bien et on lance le dessin du carré de niveau -1
        right(45)
        trace_carre_rec(cote_carre / c, nb_carres - 1) # Appel récursif
    pen_rstyle(cote_carre)
    # On poursuit le tracé du carré
    forward(cote_carre/2)
    for i in range(3):
        right(90)
        forward(cote_carre)
    right(45) # On se place bien pour éventuellement compléter le carré de degré supérieur

# Phase d'initialisation
a = 300 #Taille du côté d'origine
n = 16 # Profondeur maximale

colormode(1)
clearscreen()
up()
goto(-a//2,a//2)
pensize(2)
down() # Abaisse le crayon pour pouvoir laisser une trace
speed(0)

#Corps du programme
trace_carre_rec(a, n-1)

exitonclick()
# Ferme la fenêtre générée par turtle
mainloop()

