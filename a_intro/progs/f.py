import random as rd
""" Ce commentaire n'a aucun intérêt
    Il est juste là pour placer la chaîne 'while'
    et voir s'il est détecté ou pas.
"""

l = []
for i in range(20):
    l.append(rd.randint(1,100))
    
print(l)

def max_rec(l, m):
    if l[0] > m:
        m = l[0]
    if len(l) > 1:
        m = max_rec(l[1:], m)
    return m

n = max_rec(l,l[0])
print(n)
