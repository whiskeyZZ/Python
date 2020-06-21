tueren = []
offen = []
geschlossen = []

i = 0 

while i < 100:
    tueren.append("G")
    i += 1

y = 1
z = 1
while y <= len(tueren):
    while z <= len(tueren):
        if z % y == 0 and y % 2 == 1:
            tueren[z-1] = "O"
        if z % y == 0 and y % 2 == 0:
            tueren[z-1] = "G"
        z += 1
    z = 1
    y += 1

b = 0
print(tueren)

for e in tueren:
    if tueren[b] == "O":
        offen.append(b+1)
    else:
        geschlossen.append(b+1)
    b += 1

print("Anzahl Türen offen: " + str(len(offen)))
print(offen)
print("Anzahl Türen geschlossen: " + str(len(geschlossen)))
print(geschlossen)



