import random
import time

spieler_1 = input("Wie heißt Spieler 1 ? ")
spieler_2 = input("Wie heißt Spieler 2 ? ")

spielerwahl = random.randint(1,2)

if spielerwahl == 1:
    print(spieler_1 + " beginnt")

else:
    print(spieler_2 + " beginnt") 

punkte_sp1 = 0
punkte_sp2 = 0

while punkte_sp1 < 21 and punkte_sp2 < 21:
    a = random.randrange(1,7)
    if a == 1:
        beute = random.randint(1,2)
        l = [*range(1,9)]
        print("Gewinnchance: 80%\nMögliche Punkte: 1 bis 2")
    if a == 2:
        beute = random.randrange(1,3)
        l = [*range(1,8)]
        print("Gewinnchance: 70%\nMögliche Punkte: 1 bis 3")
    if a == 3:
        beute = random.randint(3,4)
        l = [*range(1,7)]
        print("Gewinnchance: 60%\nMögliche Punkte: 3 bis 4")
    if a == 4:
        beute = random.randrange(4,5)
        l = [*range(1,6)]
        print("Gewinnchance: 50%\nMögliche Punkte: 4 bis 6")
    if a == 5:
        beute = random.randrange(5,7)
        l = [*range(1,5)]
        print("Gewinnchance: 40%\nMögliche Punkte: 5 bis 7")
    if a == 6:
        beute = random.randint(7,8)
        l = [*range(1,4)]
        print("Gewinnchance: 30%\nMögliche Punkte: 7 bis 8")
    if a == 7:
        beute = random.randrange(8,10)
        l = [*range(1,3)]
        print("Gewinnchance: 20%\nMögliche Punkte: 8 bis 10")
    answer = 0
    while answer not in (1, 2):
        answer = int(input("Möchtest du es riskieren? '1' für Ja '2' für Nein "))
    if answer == 2:
        if spielerwahl == 1:
            spielerwahl = 2
            print(spieler_2 + " ist dran")
        else:
            spielerwahl = 1
            print(spieler_1 + " ist dran")
    if answer == 1:
        v = random.randrange(1,10)
        if v in l:
            print("Gewonnen!!! Du erhälst " + str(beute) + " Punkte")
            time.sleep(1)
            if spielerwahl == 1:
                punkte_sp1 += beute
            else:
                punkte_sp2 += beute
            print(spieler_1 + ": " + str(punkte_sp1))
            print(spieler_2 + ": " + str(punkte_sp2))
        else:
            print("Du hast verloren. Dein Gegner erhält " + str(beute) + " Punkte")
            time.sleep(1)
            if spielerwahl == 1:
                punkte_sp2 += beute
            else:
                punkte_sp1 += beute
            print(spieler_1 + ": " + str(punkte_sp1))
            print(spieler_2 + ": " + str(punkte_sp2))            
            time.sleep(1)
            if spielerwahl == 1:
                spielerwahl = 2
                print(spieler_2 + " ist dran")
            else:
                spielerwahl = 1 
                print(spieler_1 + " ist dran")

if punkte_sp1 > punkte_sp2:
    print(spieler_1 + " gewinnt!")
else:
    print(spieler_2 + " gewinnt!")





