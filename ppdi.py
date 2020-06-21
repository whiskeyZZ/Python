zahlenliste = list(range(100,1000))
print(zahlenliste)
s = 0

for i in zahlenliste:
    zahl = zahlenliste[s]
    testzahl = list(map(int, str(zahl)))
    s += 1
    ergebnis = 0
    for y in testzahl:
        ergebnis += y ** 3

    if ergebnis == zahl:
        print(zahl)

