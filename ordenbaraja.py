import random

numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
oros = [f"{x} O" for x in numeros]
copas = [f"{x} C" for x in numeros]
espadas = [f"{x} E" for x in numeros]
bastos = [f"{x} B" for x in numeros]

baraja = oros + espadas + copas + bastos
random.shuffle(baraja)
baraja_ordenada = []

o = []
c = []
e = []
b = []

for x in baraja:
    if x[-1] == "E":
        e.append(x)
    elif x[-1] == "O":
        o.append(x)
    elif x[-1] == "C":
        c.append(x)
    else:
        b.append(x)

for x in o, c, b, e:
    f = x[0][-1]
    a = [int(i[:2]) for i in x]
    d = a.copy()
    d.sort()
    b = 0
    while True:
        if a == d:
            break
        if a[b] > a[b+1]:
            c = a[b+1]
            a[b+1] = a[b]
            a[b] = c
        b += 1
        if b == 9:
            b = 0
    h = [f"{i} {f}" for i in a]
    baraja_ordenada.append(h)

baraja_ordenada = baraja_ordenada[0] +baraja_ordenada[1] + baraja_ordenada[2] + baraja_ordenada[3]

print(baraja_ordenada)
