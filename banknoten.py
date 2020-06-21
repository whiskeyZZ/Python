ungueltig = True
alphabet = ["A", "B", "C", "D", "E", "F"]

while ungueltig:
    nummer = input("Gebe eine Seriennummmer mit einem Buchstaben am Anfang und 11 Zahlen ein: ")
    l = []
    for i in nummer:
        l.append(i)
    
    if len(l) == 12 and l[0] in alphabet:
        ungueltig = False

summe = 0

for e in alphabet:
    summe += 1 
    if e == nummer[0]:
        break 

for b in range(1,len(l)-1):
    summe += int(l[b])

print(summe) 

rest = summe % 9 

if 8 - rest == 0:
    J = 9 
else:
    J = 8 - rest 

if J == int(l[11]):
    print("Die Seriennummer ist gültig")
else:
    print("Es handelt sich um eine Fälschung")










