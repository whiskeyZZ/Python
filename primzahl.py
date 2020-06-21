def sieb():
    liste = list(range(2, 120))
    nummer = 1
    for y in liste:
        i = nummer
        while i in range(nummer,len(liste)):
            if liste[i] % y == 0:
                del(liste[i])
            else:
                i += 1
        nummer += 1
    print(liste)

sieb()

        