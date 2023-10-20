import random
import time

chars = "abcdefghijklmnopqrstuvwxyz1234567890+#-"
password = ""

print("Willkommen im Password-Generator")
print("Programmiert von Oskar Frej")
time.sleep(1)

length = int(input("Wie viele Stellen soll dein Passwort haben: "))

for i in range(length+1):
    password += random.choice(chars)

print("Dein neues Passwort lautet: " + password)