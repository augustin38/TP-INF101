# 1ere version du programme :

print("Premier programme")
nom = input("Donnez votre nom : ")
print("Bonjour", nom)

# On implante une erreur dans le code :

print(Premier programme) # il manque les "" pour le texte
nom = input"Donnez votre nom : " # il manque les () du input
print("Bonjour", nom)

# Deuxième version du programme :

print("Premier programme, deuxième version")
nom = input("Donnez votre nom en majuscules : ")
print("Bonjour", nom, "comment vas-tu ?")

# programme pour échanger les valeurs de deux variables corrigé :

print("Entrez deux reels :")
x = float(input())
y = float(input())
print("Vous avez saisi ",x," et ", y)
z = x  # on ajoute la variable temporaire z pour garder en memoire la valeur de x durant l'echange.
x = y
y = z
print("Après echange des variables : ",x , " et ",y)

# Un peu d’arithmétique Q1 :

print("Calcul de la somme de 2 nombres entiers")
a = int(input("Donner un nombre : "))
b = int(input("Donner un autre nombre : "))
somme = a + b
if a >= b: # afin d'éviter d'avoir une difference negative ou faussée
    diff = a - b
else:
    diff = b - a
produit = a * b
print("La somme est : ", somme, "La difference est : ", diff, "et le produit est : ", produit)

# un peu d'arithmétique Q2 :

print("Comparaison de 2 nombres entiers")
a = int(input("Donner un nombre : "))
b = int(input("Donner un autre nombre : "))
if a == b: # teste l'egalité des entiers
    print("les deux nombres sont egaux.")
else:
    print("les deux nombres sonts differents.")

# un peu d'arithmétique Q3 :

print("division euclidiene de 2 nombres entiers")
a = int(input("Donner un nombre (numerateur): "))
b = int(input("Donner un autre nombre (denominateur, non nul): "))
if b == 0 : # evite au programme de beuguer
    print("Erreur, division par zéro impossible.")
else: # si b n'est pas nul, alors on peut effectuer les operations sans erreur
    quotient = a // b
    reste = a % b
    print("Le quotient de", a, "par", b, "est : ", quotient, ". Le reste est ", reste)

# Jeux de dés (DeuxDés)

d1 = int(input("Donner la valeur du premier dé : "))
if d1 >= 1 and d1 <= 6: # teste si l'entier correspond au valeurs d'un dé a jouer
    print("La valeur du premier dé est correcte")
    verif = 1
d2 = int(input("Donner la valeur du deuxieme dé : "))
if d2 >= 1 and d2 <= 6:
    print("La valeur du deuxieme dé est correcte")
    verif += 1
if verif == 2: # verifie que les deux dés sont conformes
    if d1 >= d2: # determine quel dé est le plus grand pour les afficher en ordre décroissant
        print("Les dés classés en ordre décroissant sont :", d1, d2)
    else:
        print("Les dés classés en ordre décroissant sont :", d2, d1)
else:
    print("les dés n'ont pas été classés car les valeurs ne correspondent pas au critères (valeurs entre 1 et 6)")

#Jeux de dés (TroisDés)

d1 = int(input("Donner la valeur du premier dé : "))
if d1 >= 1 and d1 <= 6: # teste si l'entier correspond au valeurs d'un dé a jouer
    print("La valeur du premier dé est correcte")
    verif = 1
d2 = int(input("Donner la valeur du deuxieme dé : "))
if d2 >= 1 and d2 <= 6:
    print("La valeur du deuxieme dé est correcte")
    verif += 1
d3 = int(input("Donner la valeur du troisieme dé : "))
if d3 >= 1 and d3 <= 6:
    print("La valeur du troisieme dé est correcte")
    verif += 1
if verif == 3: # verifie que les trois dés sont conformes (si l'un des dés n'a pas verifié les conditions, le total de verif n'est pas 3)
    if d1 >= d2: # tests pour determiner l'odre des trois dés 
        maxi = d1
        if d2 >= d3:
            mid = d2
            mini = d3
        else:
            mid = d3
            mini = d2
    elif d2 >= d3:
        maxi = d2
        if d1 >= d3:
            mid = d1
            mini = d3
        else:
            mid = d3
            mini = d1
    else:
        maxi = d3
        mid = d2
        mini = d1
    print("Les trois dés classés en ordre décroissant sont :", maxi, mid, mini)
    if maxi == 4 and mid == 2 and mini == 1: # teste si les valeurs sont 4 , 2 et 1
        print("Gagné !")
    else:
        print("Perdu !")

#Calcul de la moyenne et de la mention d’un étudiant (version 1) :

m_Chi = int(input("Moyenne de Chimie : "))
m_Phy = int(input("Moyenne de Physique : "))
m_Math = int(input("Moyenne de Mathématiques : "))
m_Inf = int(input("Moyenne d'Informatique : "))
if (m_Chi >= 0 and m_Chi <= 20) and (m_Phy >= 0 and m_Phy <= 20) and (m_Math >= 0 and m_Math <= 20) and (m_Inf >= 0 and m_Inf <= 20): # verification que toutes les notes sont entre 0 et 20
    m_totale = (m_Chi + m_Phy + m_Math + m_Inf) / 4 # clacul de la moyenne
    print("moyenne des 4 matières : ", m_totale)
else:
    print("INCORRECT")

#Calcul de la moyenne et de la mention d’un étudiant (version 2) :

m_Chi = int(input("Moyenne de Chimie : "))
if m_Chi >= 0 and m_Chi <= 20: # verification que la notes est entre 0 et 20
    m_Phy = int(input("Moyenne de Physique : "))
    if m_Phy >= 0 and m_Phy <= 20: # plusieurs niveaux de if pour que le programme s'arrete si une note n'est pas bonne sans demander les autres notes
        m_Math = int(input("Moyenne de Mathématiques"))
        if m_Math >= 0 and m_Math <= 20:
            m_Inf = int(input("Moyenne d'Informatique"))
            if m_Inf >= 0 and m_Inf <= 20:
                m_totale = (m_Chi + m_Phy + m_Math + m_Inf) / 4
                print("moyenne des 4 matières : ", m_totale)
            else:
                print("INCORRECT")
        else: # chaque else est associé au test d'une matière
            print("INCORRECT")
    else:
        print("INCORRECT")
else:
    print("INCORRECT")

#Calcul de la moyenne et de la mention d’un étudiant (version 3) :

m_Chi = int(input("Moyenne de Chimie : "))
m_Phy = int(input("Moyenne de Physique : "))
m_Math = int(input("Moyenne de Mathématiques : "))
m_Inf = int(input("Moyenne d'Informatique : "))
if (m_Chi >= 0 and m_Chi <= 20) and (m_Phy >= 0 and m_Phy <= 20) and (m_Math >= 0 and m_Math <= 20) and (m_Inf >= 0 and m_Inf <= 20): # verification que toutes les notes sont entre 0 et 20
    m_totale = ((m_Chi*3) + (m_Phy*4) + (m_Math*2) + (m_Inf*2)) / 11 # calcul de la moyenne avec chaque matiere fois son coeff, divisé par le total de coeffs
    print("moyenne des 4 matières : ", m_totale)
else:
    print("INCORRECT")

# #Calcul de la moyenne et de la mention d’un étudiant (version 4) :

m_Chi = int(input("Moyenne de Chimie : "))
m_Phy = int(input("Moyenne de Physique : "))
m_Math = int(input("Moyenne de Mathématiques : "))
m_Inf = int(input("Moyenne d'Informatique : "))
if (m_Chi >= 0 and m_Chi <= 20) and (m_Phy >= 0 and m_Phy <= 20) and (m_Math >= 0 and m_Math <= 20) and (m_Inf >= 0 and m_Inf <= 20): # verification que toutes les notes sont entre 0 et 20
    m_totale = ((m_Chi*3) + (m_Phy*4) + (m_Math*2) + (m_Inf*2)) / 11 # calcul de la moyenne avec chaque matiere fois son coeff, divisé par le total de coeffs
    if m_totale < 10: # on determine le statut de l'etudiant suivant sa moyenne
        statut = "AJOURNE"
    elif m_totale < 12:
        statut = "PASSABLE"
    elif m_totale < 14:
        statut = "ASSEZ BIEN"
    elif m_totale < 16:
        statut = "BIEN"
    else:
        statut = "TRES BIEN"
    print("moyenne des 4 matières : ", m_totale, "votre statut est : ", statut)
else:
    print("INCORRECT")

#Calcul de la moyenne et de la mention d’un étudiant (version 5) :

m_Chi = int(input("Moyenne de Chimie : "))
m_Phy = int(input("Moyenne de Physique : "))
m_Math = int(input("Moyenne de Mathématiques : "))
m_Inf = int(input("Moyenne d'Informatique : "))
if (m_Chi >= 0 and m_Chi <= 20) and (m_Phy >= 0 and m_Phy <= 20) and (m_Math >= 0 and m_Math <= 20) and (m_Inf >= 0 and m_Inf <= 20): # verification que toutes les notes sont entre 0 et 20
    m_totale = ((m_Chi*3) + (m_Phy*4) + (m_Math*2) + (m_Inf*2)) / 11 # calcul de la moyenne avec chaque matiere fois son coeff, divisé par le total de coeffs
    if m_totale < 10: # on determine le statut de l'etudiant suivant sa moyenne
        statut = "AJOURNE"
    elif m_totale < 12:
        statut = "PASSABLE"
    elif m_totale < 14:
        statut = "ASSEZ BIEN"
    elif m_totale < 16:
        statut = "BIEN"
    else:
        statut = "TRES BIEN"
    print("moyenne des 4 matières : ", m_totale, "votre statut est : ", statut)
else: # on rejoue le programme pour avoir une deuxieme chance
    print("INCORRECT")
    print("vous avez le droit a une deuxieme chance, saisissez a nouveau vos notes :")
    m_Chi = int(input("Moyenne de Chimie : "))
    m_Phy = int(input("Moyenne de Physique : "))
    m_Math = int(input("Moyenne de Mathématiques : "))
    m_Inf = int(input("Moyenne d'Informatique : "))
    if (m_Chi >= 0 and m_Chi <= 20) and (m_Phy >= 0 and m_Phy <= 20) and (m_Math >= 0 and m_Math <= 20) and (m_Inf >= 0 and m_Inf <= 20): # verification que toutes les notes sont entre 0 et 20
        m_totale = ((m_Chi*3) + (m_Phy*4) + (m_Math*2) + (m_Inf*2)) / 11 # calcul de la moyenne avec chaque matiere fois son coeff, divisé par le total de coeffs
        if m_totale < 10:
            statut = "AJOURNE"
        elif m_totale < 12:
            statut = "PASSABLE"
        elif m_totale < 14:
            statut = "ASSEZ BIEN"
        elif m_totale < 16:
            statut = "BIEN"
        else:
            statut = "TRES BIEN"
        print("moyenne des 4 matières : ", m_totale, "votre statut est : ", statut)

#Calcul de la moyenne et de la mention d’un étudiant (version 6) :

while verif:
    m_Chi = int(input("Moyenne de Chimie : "))
    m_Phy = int(input("Moyenne de Physique : "))
    m_Math = int(input("Moyenne de Mathématiques : "))
    m_Inf = int(input("Moyenne d'Informatique : "))
    if (m_Chi >= 0 and m_Chi <= 20) and (m_Phy >= 0 and m_Phy <= 20) and (m_Math >= 0 and m_Math <= 20) and (m_Inf >= 0 and m_Inf <= 20): # verification que toutes les notes sont entre 0 et 20
        m_totale = ((m_Chi*3) + (m_Phy*4) + (m_Math*2) + (m_Inf*2)) / 11 # calcul de la moyenne avec chaque matiere fois son coeff, divisé par le total de coeffs
        if m_totale < 10: # on determine le statut de l'etudiant suivant sa moyenne
            statut = "AJOURNE"
        elif m_totale < 12:
            statut = "PASSABLE"
        elif m_totale < 14:
            statut = "ASSEZ BIEN"
        elif m_totale < 16:
            statut = "BIEN"
        else:
            statut = "TRES BIEN"
        print("moyenne des 4 matières : ", m_totale, "votre statut est : ", statut)
        verif = False
    else:
        print("INCORRECT")
        print("recommencez, saisissez vos notes : ")

# trigonometrie :

from math import *
h = int(input("entrez une valeur de l'hypothenuse : "))
a = float(input("entrez la valeur d'un angle : "))
opp = sin(a) * h # on calcule la longueur du coté opposé a l'aide des formules de trigo
adj = cos(a) * h # on calcule la longueur du coté adjacent a l'aide des formules de trigo
print("Les deux côtés sont: ", opp, " , ", adj)
if (h**2) == (opp**2 + adj**2): # on verifie le théoreme de pythagore (infonctionel a cause les float)
    print("les valeurs données verifient bien le théorème de pythagore")
else:
    print("les valeurs données ne verifient pas le théorème de pythagore")

# polynome :

while verif:
    a = int(input("donner un entier a :"))
    b = int(input("donner un entier b :"))
    c = int(input("donner un entier c :"))
    delta = (b**2) - 4*(a*c) # on calcule delta
    if delta > 0:
        r1 = (((-b)+sqrt(delta))/2*a) # doubles racines si delta est positif
        r2 = (((-b)-sqrt(delta))/2*a)
    elif delta == 0:
        r0 = ((-b)/2*a) # racine unique si delta est nul

# random

from random import *
a = int(input("donner un entier a"))
b = int(input("donner un entier b"))
if a < b:
    nb = random.randint(a, b) # choisi un nombre aléatoire entre a et b
else :
    nb = random.randint(b, a) # choisi un nombre aléatoire entre b et a
print("un nombre aléatoire entre a et b :", nb)
