import random as rd

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