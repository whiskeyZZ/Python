import random
import time 

coins = 1000
moeglichkeiten = list(range(1,37))
print("Willkommen beim Roulette!")
time.sleep(1)

while coins > 0:
    print("Du hast " + str(coins) + " Coins")
    time.sleep(1)
    einsatz = int(input("Wie viel möchtest du setzen? "))
    while einsatz > coins:
        einsatz = int(input("Wie viel möchtest du setzen? "))
    print("Worauf möchtest du setzen?")
    time.sleep(1)
    auswahl = True
    while auswahl:
        bet = input("Wähle eine Zahl zwischen 1 und 36 oder wähle 'rot oder 'schwarz' ")
        try:
            if int(bet) in moeglichkeiten:
                auswahl = False
                a = 1
        except ValueError:
            if bet == "rot" or bet == "schwarz":
                auswahl = False
                a = 2
    
    if a == 1:
        print("Nichts geht mehr!")
        time.sleep(1)
        print("......")
        time.sleep(1)
        zahl = random.choice(moeglichkeiten)
        print(str(zahl) + "!")
        if zahl == int(bet):
            coins += 36*einsatz
            print("Du hast gewonnen")
        else:
            coins -= einsatz
            print("Du hast verloren")

    if a == 2:
        print("Nichts geht mehr!")
        time.sleep(1)
        print("......")
        time.sleep(1)
        farbe = random.randint(1,2)
        if farbe == 1:
            print("Rot!")
            if bet == "rot":
                coins += einsatz
                print("Du hast gewonnen")
            else:
                coins -= einsatz
                print("Du hast verloren")
        if farbe == 2:
            print("Schwarz!")
            if bet == "schwarz":
                coins += einsatz
                print("Du hast gewonnen")
            else:
                coins -= einsatz
                print("Du hast verloren")
time.sleep(1)
print("Du bist pleite")


        
