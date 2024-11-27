from random import *
from copy import *

# Exercice 1:

def creation(n):
    nature = ["C"]
    for i in range(n-1):
        nature.append("I")
    return nature

def rencontre(n):
    X = randint(0,n-1)
    Y = randint(0,n-1)
    while Y == X:
        Y = randint(0,n-1)
    return X, Y

def transformation(n, nature, X, Y):
    if nature[X] == nature[Y] == "C":
        nature[X] = "M"
        nature[Y] = "M"
    elif (nature[X] == "C" and nature[Y] == "I") or (nature[X] == "I" and nature[Y] == "C"):
        nature[X] = "C"
        nature[Y] = "C"
    elif (nature[X] == "C" and nature[Y] == "M") or (nature[X] == "M" and nature[Y] == "C"):
        nature[X] = "M"
        nature[Y] = "M"
    return nature

def evolue(nature):
    for e in nature:
        if e == "C":
            return True
    return False

def affichage(n, nature, ancien_nature, day, X, Y):
    if day < 10:
        day = " " + str(day)
    print(day, 5*" ", X, ",   ", Y, 4*" ", nature[X], ", ", nature[Y], 4*" ", sep = "", end = "")
    for e in range(len(nature)):
        if nature[e] == ancien_nature[e]:
            print("-", 3*" ", end ="")
        else:
            print(nature[e], 3*" ", end ="")
    print("")
    
def affichage_start(n, nature):
    print("Jour Rencontre Nature", end = "  ")
    for a in range(n):
        print("st.", a, sep = "" ,end = " ")
    print("\n 0", 22*" ", end = "")
    for e in nature:
        print(e, 3*" ", end ="")
    print("")

def compte_final(nature):
    i = 0 ; m = 0
    for e in nature:
        if e == "I":
            i+=1
        if e == "M":
            m +=1
    return i, m

def principal():
    n = int(input("population N : "))
    day = 0
    nature = creation(n)
    affichage_start(n, nature)
    while evolue(nature):
        X, Y = rencontre(n)
        ancien_nature = copy(nature)
        nature = transformation(n, nature, X, Y)
        affichage(n, nature, ancien_nature, day, X, Y)
        day += 1
    i, m = compte_final(nature)
    print("Nombre d'ignorants : ", i)
    print("Nombre de muets : ", m)


# Exercice 2:

def principalv2():
    n = int(input("population N : "))
    day = 0
    nature = creation(n)
    while evolue(nature):
        X, Y = rencontre(n)
        nature = transformation(n, nature, X, Y)
        day += 1
    i, m = compte_final(nature)
    print("NJ : ", day, "NI : ", i)

# Exercice 3:

def principalv3(n):
    day = 0
    nature = creation(n)
    while evolue(nature):
        X, Y = rencontre(n)
        nature = transformation(n, nature, X, Y)
        day += 1
    i, m = compte_final(nature)
    return day, i

def stats_simulation():
    n = int(input("population N : "))
    nf = int(input("Nombre de simulations NF : "))
    moyd = 0
    moyi = 0
    for a in range(nf):
        day, i = principalv3(n)
        moyd += day
        moyi += i
    moyd /= a
    moyi /= a
    print("Moyenne jours : ", moyd, " -  Moyenne ignorants : ", moyi)


# Exercice 4:

def affichage_startv2(n, nature):
    print("Jour Rencontre Nature", end = "  ")
    for a in range(n):
        print("st.", a, sep = "" ,end = " ")
    print("repartition")
    print(" 0", 22*" ", end = "")
    for e in nature:
        print(e, 3*" ", end ="")
    print("")

def affichagev2(n, nature, ancien_nature, day, X, Y, NC, NM, NI):
    if day < 10:
        day = " " + str(day)
    print(day, 5*" ", X, ",   ", Y, 4*" ", nature[X], ", ", nature[Y], 4*" ", sep = "", end = "")
    for e in range(len(nature)):
        if nature[e] == ancien_nature[e]:
            print("-", 3*" ", end ="")
        else:
            print(nature[e], 3*" ", end ="")
    print("#"*NC, "*"*NM, "."*NI, sep = "")

def pourcentage(nature):
    NC = 0
    NM = 0
    NI = 0
    for e in nature:
        if e == "C":
            NC += 1
        elif e == "M":
            NM += 1
        else:
            NI += 1
    return NC, NM, NI


def principalv4():
    n = int(input("population N : "))
    day = 0
    nature = creation(n)
    affichage_startv2(n, nature)
    while evolue(nature):
        X, Y = rencontre(n)
        ancien_nature = copy(nature)
        nature = transformation(n, nature, X, Y)
        NC, NM, NI = pourcentage(nature)
        affichagev2(n, nature, ancien_nature, day, X, Y, NC, NM, NI)
        day += 1
    i, m = compte_final(nature)
    print("Nombre d'ignorants : ", i)
    print("Nombre de muets : ", m)


