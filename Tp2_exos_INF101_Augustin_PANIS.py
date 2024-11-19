# Le jeu de base : (version 1)

from random import *
n = random.randint(0, 100)
rep = int(input("Devine mon nombre entre 0 et 100 : "))
while rep != n:
    print("perdu ! Réessayez")
    rep = int(input("Devine mon nombre entre 0 et 100 : "))
print("Gagné !")

# Le jeu de base : (version 2)

from random import *
n = random.randint(0, 100)
mino = 0
majo = 100
rep = int(input("Devine mon nombre entre", mino, "et", majo ": "))
while rep != n:
    if rep < n:
        print("Trop petit")
        mino = rep + 1
    else:
        print("trop grand")
        majo = rep - 1
    rep = int(input("Devine mon nombre entre", mino, "et", majo ": "))
print("Gagné !")

# Le jeu de base : (version 3)

from random import *
n = random.randint(0, 100)
mino = 0
majo = 100
rep = int(input("Devine mon nombre entre", mino, "et", majo ": "))
while rep != n and i <= 5:
    if rep < n:
        print("Trop petit")
        mino = rep + 1
    else:
        print("trop grand")
        majo = rep - 1
    rep = int(input("Devine mon nombre entre", mino, "et", majo ": "))
    i += 1
if i <= 5:
    print("Gagné au bout de", i "essais !")
else:
    print("Perdu !")

# Le jeu de base : (version 4)

from random import *
n = random.randint(0, 100)
mino = 0
majo = 100
i = 1
rep = int(input("Devine mon nombre entre", mino, "et", majo, "(", (6-i)"essais) : "))
while rep != n and i <= 5:
    if rep < n:
        print("Trop petit")
        mino = rep + 1
    else:
        print("trop grand")
        majo = rep - 1
    i += 1
    rep = int(input("Devine mon nombre entre", mino, "et", majo, "(", (6-i)"essais) : "))
if i <= 5:
    print("Gagné au bout de", i "essais !")
else:
    print("Perdu !")

# Le jeu de base : (version 5)

from random import *
play = True
while play:
    n = random.randint(0, 100)
    mino = 0
    majo = 100
    i = 1
    win = 0
    parties = 0
    moyenne_essais = 0
    rep = int(input("Devine mon nombre entre", mino, "et", majo, "(", (6-i)"essais) : "))
    while rep != n and i <= 5:
        if rep < n:
            print("Trop petit")
            mino = rep + 1
        else:
            print("trop grand")
            majo = rep - 1
        i += 1
        rep = int(input("Devine mon nombre entre", mino, "et", majo, "(", (6-i)"essais) : "))
    parties += 1
    if i <= 5:
        print("Gagné au bout de", i "essais !")
        win += 1
        moyenne_essais += i
    else:
        print("Perdu !")
    val_play = input("voulez-vous recommencer ? (o/n)")
    if val_play != "o":
        play = False
if moyenne_essais == 0:
    moyenne_essais = 1
moyenne_essais = moyenne_essais / win
print("tu as gagné", win, "parties sur", parties, "jouées")
if win >= 1:
    print("tu as mis en moyenne", moyenne_essais, "essais pour deviner")

# Une IA pour le prix du gros lot : (version 1)

mino = 0
majo = 100
val = random.randint(mino, majo)
print("Je cherche un nombre entre", mino, "et", majo)
rep = int(input("Je propose", val "? "))
while rep != "b":
    if rep == "p":
        mino = val + 1
        print("Je cherche un nombre entre", mino, "et", majo)
    elif rep == "g":
        majo = val - 1
        print("Je cherche un nombre entre", mino, "et", majo)
    val = random.randint(mino, majo)
    rep = int(input("Je propose", val "? "))
print("J'ai gagné")

# Une IA pour le prix du gros lot : (version 2)

n = random.randint(0, 100)
mino = 0
majo = 100
val = random.randint(mino, majo)
i = 1
print("Je cherche un nombre entre", mino, "et", majo)
print("Je propose", val ": ", end =" ")
while val != n:
    if val < n:
        mino = val + 1
        print("p")
    elif val > n:
        majo = val - 1
        print("g")
    val = random.randint(mino, majo)
    print("Je propose", val ": ", end =" ")
    i += 1
print("J'ai gagné en", i, "essais.")

# Une IA pour le prix du gros lot : (version 3)

parties = int(input("nombre de parties :"))
moyenne_essais = 0
for a in range(parties):
    n = random.randint(0, 100)
    mino = 0
    majo = 100
    val = random.randint(mino, majo)
    i = 1
    print("Je cherche un nombre entre", mino, "et", majo)
    print("Je propose", val ": ", end =" ")
    while val != n:
        if val < n:
            mino = val + 1
            print("p")
        elif val > n:
            majo = val - 1
            print("g")
        val = random.randint(mino, majo)
        print("Je propose", val ": ", end =" ")
        i += 1
    print("J'ai gagné en", i, "essais.")
    moyenne_essais += i
moyenne_essais = moyenne_essais / (a+1)
print("nombre moyen d'essais par partie gagnée :", moyenne_essais)

# Une IA pour le prix du gros lot : (version 4)

parties = int(input("nombre de parties :"))
moyenne_essais = 0
for a in range(parties):
    n = random.randint(0, 100)
    mino = 0
    majo = 100
    val = (mino + mano) / 2
    i = 1
    print("Je cherche un nombre entre", mino, "et", majo)
    print("Je propose", val ": ", end =" ")
    while val != n:
        if val < n:
            mino = val + 1
            print("p")
        elif val > n:
            majo = val - 1
            print("g")
        val = (mino + mano) / 2
        print("Je propose", val ": ", end =" ")
        i += 1
    print("J'ai gagné en", i, "essais.")
    moyenne_essais += i
moyenne_essais = moyenne_essais / (a+1)
print("nombre moyen d'essais par partie gagnée :", moyenne_essais)

# Une IA pour le prix du gros lot : (Question 5)

# lorsque le nombre de parties n est faible, on remarque que l'IA non optimisée obtient des resultats aléatoires
# parfois meilleurs mais très souvent moins bons que l'autre IA,
# alors que l'IA optimisée obtient des resultats toujours très similaires.
# Aussi, lorsque le nombre de parties n est grand, on remarque que l'IA non optimisée est beaucoups moins efficace que l'IA optimisée

# Une IA pour le prix du gros lot : (version 6)

parties = int(input("nombre de parties :"))
moyenne_essais_opti = 0
moyenne_essais = 0
for numero in range(0, 100):
    for a in range(parties):
        n = numero
        mino = 0
        majo = 100
        val = (mino + mano) / 2
        i = 1
        j = 1
        while val != n:
            if val < n:
                mino = val + 1
            elif val > n:
                majo = val - 1
            val = (mino + mano) / 2
            i += 1
        moyenne_essais_opti += i
        val = random.randint(mino, majo)
        while val != n:
            if val < n:
                mino = val + 1
            elif val > n:
                majo = val - 1
            val = random.randint(mino, majo)
            j += 1
        moyenne_essais += j
    moyenne_essais = moyenne_essais / (a+1)
    moyenne_essais_opti = moyenne_essais_opti / (a+1)
    print("nombre secret = ", numero)
    print("moyenne d'essais de l'IA non optimisée :", moyenne_essais)
    print("moyenne d'essais de l'IA optimisée :", moyenne_essais_opti)

# Une IA pour le prix du gros lot : (version 7)

parties = int(input("nombre de parties :"))
moyenne_essais_opti = 0
moyenne_essais = 0
for numero in range(0, 100):
    for a in range(parties):
        n = numero
        mino = 0
        majo = 100
        val = (mino + mano) / 2
        i = 1
        j = 1
        while val != n:
            if val < n:
                mino = val + 1
            elif val > n:
                majo = val - 1
            val = (mino + mano) / 2
            i += 1
        moyenne_essais_opti += i
        val = random.randint(mino, majo)
        while val != n:
            if val < n:
                mino = val + 1
            elif val > n:
                majo = val - 1
            val = random.randint(mino, majo)
            j += 1
        moyenne_essais += j
    moyenne_essais = moyenne_essais / (a+1)
    moyenne_essais_opti = moyenne_essais_opti / (a+1)
    print("[", numero, "]", sep="", end=" ")
    print("*"*moyenne_essais_opti)
    print("-"*moyenne_essais)

# On remarque que l'ia intelligente est beaucoup plus efficace au global, mais se rapproche de l'ia aléatoire
# voir est moins efficace que celle ci sur certaines valeurs qui sont les extremités des bornes.