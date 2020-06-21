geschlossen = list(range(1,101))
offen = []


i = 1

while i < 101:
    if i % 2 != 0:
        for x in range(0,len(geschlossen),i):
            offen.append(geschlossen[x])
            geschlossen[x] = 0
        x = 0
        while x in range(len(geschlossen)):
            if geschlossen[x] in offen:
                del(geschlossen[x])
            else:
                x += 1
        geschlossen.sort()
        offen.sort()

    else:
        for x in range(0,len(offen),i):
            geschlossen.append(offen[x])
            offen[x] = 0
        x = 0
        while x in range(len(offen)):
            if offen[x] in geschlossen:
                del(offen[x])
            else:
                x += 1
        geschlossen.sort()
        offen.sort()

    i += 1


print(offen)

