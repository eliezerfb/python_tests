def gerador():
    i = 0
    print('Inicio')
    while i < 10:
        i += 1
        yield i
    print('Fim')

    
g = gerador()

next(g)
next(g)
next(g)

for g in gerador():
    print(g)