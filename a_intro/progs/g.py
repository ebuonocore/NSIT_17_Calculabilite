import random as rd
# Création d'une liste aléatoire
l = []
for i in range(20):
    l.append(rd.randint(-100,100))
    
print(l) # Affiche la liste créée


def liste_sans_tete(ma_liste:list):
    """ Prend une liste en paramètre.
        Renvoie la liste sans le premier élément.
        Précondition: La liste n'est pas vide
    """
    autre_liste = []
    for i in range(1,len(ma_liste)):
        autre_liste.append(ma_liste[i])
    return autre_liste
        
def max_rec(l, m):
    if l[0] > m:
        m = l[0]
    if len(l) > 1:
        m = max_rec(liste_sans_tete(l), m)
    return m

n = max_rec(l,l[0])
print(n)