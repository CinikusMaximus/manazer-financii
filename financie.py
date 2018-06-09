import os
#otvorí súbor "file" a vytvorí premenné
file = open("financie","r+")
a = 26
b = 1
c = 2
f = 0
suma = 0
#algoritmus na prečítanie súboru financie s údajmi o peniazoch
for x in range(14):
    typ = float(file.readline(b))
    if typ == 5.0 and f == 0:
        typ = 0.05
        f = 1
    hodnota = float(file.readline(c))
    hodnota = hodnota / 10
    suma = float(suma + typ * hodnota)
    hodnota = int(hodnota)
    hodnota = str(hodnota)
    if hodnota != "0":
        typ = str(typ)
        print(typ + "€ -> " + hodnota)
    b = b + 2
    c = c + 2
file.close()
suma = str(suma)
print("Momentalne máš: " + suma + "€")
print("\nChceš editovať?")
print("[0] NIE\n[1] Pridať\n[2] Odobrať")
d = int(input())
#ak užívateľ zvolí možnosť pridať hodnotu
if d == 1:
    file = open("financie","r+")
    file2 = open("financie2","w")
    print("Zadaj hodnotu, ktorú chceš pridať (0.10|2.00)")
    o = float(input())
    print("Zadaj koľkokrát chceš hodnotu pridať (1|5)")
    p = str(input())
    a = file.readlines()
    #algoritmus na update súboru
#premenovanie a vymazanie prebytočných suborov
file.close()
file2.close()
os.remove("financie")
os.rename('financie2', 'financie')
input()