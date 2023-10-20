import random
import time

zahl = random.randint(1,50)

print("Willkommen im Zahlen erraten.")
print("Programmiert von Oskar Frej")
time.sleep(1)

def spiel():
    guess = int(input("Wähle eine Zahl zwischen 1 und 50: "))

    def gewonnen():
        time.sleep(1)
        print("Du hast die richtige Zahl getroffen!")
        nochmalspielen()

    def verloren():
        time.sleep(1)
        print("Du hast die falsche Zahl getroffen!")
        nochmalspielen()

    def nochmalspielen():
        time.sleep(1)
        print("Möchtest du nochmal spielen?")
        time.sleep(1)
        auswahl = input("y/n: ")
        time.sleep(1)
        if auswahl == "y":
            spiel()
        else:
            print("Das Spiel wird nun beendet.")

    if guess == zahl:
        gewonnen()
    else:
        verloren()

spiel()

