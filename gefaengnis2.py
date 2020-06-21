geschlossen = list(range(1,10))
offen = []
i = 1

while i < 11:
    if i % 2 == 1:
        x = 0
        while x in range(len(geschlossen)):
            if x % i == 0:
                offen.append(geschlossen[x])
                geschlossen.remove(geschlossen[x])
            else:
                x += 1
    if i % 2 == 0:
        y = 0
        while y in range(len(offen)):
            if y % i == 0:
                geschlossen.append(offen[y])
                offen.remove(offen[y])
            else:
                y += 1
    print(offen)
    print(geschlossen)
    i += 1

