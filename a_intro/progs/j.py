# -*- coding: utf-8 -*-
"""
Créé le 02/10/2020 à 15h30
Factorielle avec tests unitaire (Doctest) et assertion

@author: Eric Buonocore
"""

def factoreille_rec(n):
    """ Renvoie factorielle n. (Qui s'écrit aussi n!)
        n doit être un entier,
        mais il faut aussi accepter les flottant avec une partie décimale nulle,
        par exemple 2.0 est accepté.

    >>> factoreille_rec(0)
    1
    >>> factoreille_rec(4)
    24
    >>> factoreille_rec(5.0)
    120

    """
    import math
    if math.floor(n) != n: # On compare la partie entière de n à n. Le flottant 5.0 par exemple est accpeté
        raise ValueError("n ne doit pas avoir de partie décimale")
    assert n >= 0, "n doit être positif."
    
    if n == 0:
        return 1
    else:
        return int(n * factoreille_rec(n-1)) # Le résultat est transtypé pour ne pas renvoyer de flottant


if __name__ == "__main__": # Corps du programme
    import doctest
    doctest.testmod(verbose = True)
    print("4! =",factoreille_rec(4))
    print("5.0! =",factoreille_rec(5.0))
    print("-1! =",factoreille_rec(-1))