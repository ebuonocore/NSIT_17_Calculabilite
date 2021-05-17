def binaire(n):
    """ Prend un entier positif en paramètre
        Affiche la conversion binaire de ce nombre décimal
    """
    assert type(n) == int, 'n doit être un entier'
    assert n >= 0, 'n doit être positif'
    if n == 0:
       return []
    quotient = n // 2
    reste = n%2
    return binaire(quotient)+[reste]

#print(binaire(13))



def conv_rec(n:int):
    """ Prend un entier positif en paramètre
        Affiche la conversion binaire de ce nombre décimal
    """
    assert type(n) == int, 'n doit être un entier'
    assert n >= 0, 'n doit être positif'
    quotient = n // 2
    reste = n%2
    if quotient > 0:
        conv_rec(quotient)
    print(reste, end="")
    

#conv_rec(0)
