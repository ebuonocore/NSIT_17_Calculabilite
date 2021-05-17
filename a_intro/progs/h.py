# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:50:29 2019
Dessine des carrés imbriqués en impératif

@author: Eric Buonocore
"""

def mystere(n):
    if n == 0:
        return 0
    else:
        return n + mystere(n-1)
    
print(mystere(3))