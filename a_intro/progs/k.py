def suivant(x:int) -> int:
    return x + 1

def double(x:int) -> int:
    return x + x

def myst(f:callable, g:callable, x:int) -> int:
    if x % 2 == 0:
        return f(x)
    return g(x)

i = 0
while i<6:
    i += 1
    print(myst(suivant, double, i), end=" ")
print()
    
i = 0
while i<6:
    i += 1
    print(myst(double,suivant, i), end=" ")
