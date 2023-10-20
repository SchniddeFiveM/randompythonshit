import time
import random
def spiel():
    global liste, Zufall
    liste = ["Schere", "Stein", "Papier"]
    Zufall = random.choice(liste)

    print(Zufall)

    print("Herzlich Willkommen zu Schere, Stein, Papier.")
    time.sleep(1)
    print("Wähle nun Schere, Stein oder Papier")

    auswahl = input("Schere, Stein oder Papier: ")

    def gewonnen():
        time.sleep(1)
        print("Du hast gewonnen!")
        time.sleep(1)
        print("Dein Gegner hatte " + Zufall)
        time.sleep(1)
        print("Möchtest du noch eine Runde spielen?")
        auswahl2 = input("y/n: ")

        if auswahl2 == "y":
            print("Das Spiel wird nun neugestartet.")
            time.sleep(1)
            spiel()
        else:
            print("Das Spiel wird nun beendet.")
            time.sleep(1)

    def verloren():
        time.sleep(1)
        print("Du hast verloren!")
        time.sleep(1)
        print("Dein Gegner hatte " + Zufall)
        time.sleep(1)
        print("Möchtest du noch eine Runde spielen?")
        auswahl2 = input("y/n: ")

        if auswahl2 == "y":
            print("Das Spiel wird nun neugestartet.")
            time.sleep(1)
            spiel()
        else:
            print("Das Spiel wird nun beendet.")
            time.sleep(1)

    def gleichstand():
        time.sleep(1)
        print("Es ist gleichstand!")
        time.sleep(1)
        print("Dein Gegner hatte " + Zufall)
        time.sleep(1)
        print("Möchtest du noch eine Runde spielen?")
        auswahl2 = input("y/n: ")

        if auswahl2 == "y":
            print("Das Spiel wird nun neugestartet.")
            time.sleep(1)
            spiel()
        else:
            print("Das Spiel wird nun beendet.")
            time.sleep(1)

    if Zufall == "Schere":
        if auswahl == "Papier":
           verloren()
        elif auswahl == "Schere":
           gleichstand()
        else:
            gewonnen()

    if Zufall == "Papier":
        if auswahl == "Stein":
            verloren()
        elif auswahl == "Papier":
            gleichstand()
        else:
            gewonnen()

    if Zufall == "Stein":
        if auswahl == "Schere":
            verloren()
        elif auswahl == "Stein":
            gleichstand()
        else:
            gewonnen()

spiel()
