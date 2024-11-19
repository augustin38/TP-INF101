from math import *
import scipy
# # Exercices d’observation : 

# # Décrire les appels de fonctions :
def est_solution(x,a,b,c): # appelée 4 fois
    y=a*x**2+b*x+c
    rep= (y==0)
    return rep

# est_solution(1,2,3,4) # aucune valeur de retour, et les arguments sont des entiers
# print(rep) # erreur : rep n'est pas definie dans le programme principal a ce moment la
# rep=est_solution(1,1,-2,1) # la valeur de retour est un entier , et les arguments sont des entiers
# print(rep)
# print(est_solution(5, 2, -20, 50)) # la valeur de retour est un entier , et les arguments sont des entiers
# print(est_solution(2.5, 1, 2, 3)) # la valeur de retour est un entier , et les arguments sont des entiers

def distance(xA,yA,xB,yB): # appelée 3 fois
    d=(xB-xA)**2+(yB-yA)**2
    d=d**(1/2)
    return d

def appartient_cercle(xA,yA,rayon): # appelée 2 fois
    return (distance(0,0,xA,yA)==rayon) # ne fait pas ce qu'on veut : xA et yA doivent etre les deux premiers indices de l'appel.
# De plus, on évite d'uttiliser les memes noms dans le programme principal que les fonctions.

# d=distance(1,2,2,1) # la valeur de retour est un entier , et les arguments sont des entiers
# print(d)
# rep=appartient_cercle(1,1,2) # la valeur de retour est un booleen , et les arguments sont des entiers
# print(rep)
# print(appartient_cercle(1,0,1)) # la valeur de retour est un booleen , et les arguments sont des entiers

# # Reconnaître les variables locales :
def est_premier(N):
    i=2 # variable locale
    a_diviseur=False # variable locale
    while i<N and (not a_diviseur):
        if N%i==0:
            a_diviseur=True
            i=i+1
    return not a_diviseur

# if __name__=="__main__":
#     rep=est_premier(9)
#     print("9 est premier ?", rep)
#     print("5 est premier ?", est_premier(5))

# # Fonction locals() :
def pente(xA, yA, xB, yB):
    p=(yB-yA)/(xB-xA)
    print("Var. loc. de pente :", locals()) # affiche p la variable locale de pente(xA, yA, xB, yB)
    return p

# # Incrémentation :
def incremente (a): # cette fonction modifie localement la valeur de a (ajout de 1)
    a = a+1

# a=5
# incremente(a)
# print (a) # a=5 car a n'a changé que localement pour la fonction.
# b=3
# incremente(b)
# print (b) # b=3 car a n'a changé que localement pour la fonction.
# a=incremente(a) # a vaut alors None car on ne recupère aucune valeur.
# print(a)


def incremente2(a): # cette fonction ajoute 1 a une valeur donnée et la renvoie
    return a+1

# a=3
# incremente2(a)
# print(a) # affiche a=3 car on n'a pas recupéré la valeur de sortie de la fonction
# b=1
# b = incremente2(b)
# print(b) # affiche b=2 car on recupère la valeur de sortie de la fonction, ou b= b + 1
# a=incremente2(b)
# print(a) # a=3 car cette valeur de retour est celle du b appelé dans la fonction, c'est a dire b=2

# # Des petites fonctions :

# # La bosse des maths :
def valeur_abs(x):
    return sqrt(x**2)

def signe_different(x, y):
    if x*y >= 0:
        return False
    else:
        return True

def f(x):
    return (3*(x**2) + 2*x + 3)

# # Polynome :
def nb_racines(a, b, c):
    d = (b**2) - (4*a*c)
    if d > 0:
        return 2
    elif d == 0:
        return 1
    else:
        return 0

def resolution(a,b,c):
    if nb_racines(a, b, c) == 2:
        x1 = (-b + sqrt((b**2) - (4*a*c))) / 2*a
        x2 = (-b - sqrt((b**2) - (4*a*c))) / 2*a
        print("Les 2 racines du polynome sont : \n x1 =", x1, "\n x2 = ", x2)
    elif nb_racines(a, b, c) == 1:
        x0 = (-b) / 2*a
        print("L'unique du polynome est : \n x0 =", x0)
    else:
        print("le polynome n'a pas de racines reelles.")

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# nb_racines(a, b, c)

# La banque Argento :
#q1
def capital(nba,deb):
    a=1
    while a <= nba:
        deb = (deb * 1.05) - 11
        a +=1
    return deb

#q2
def gagne(nba,deb):
    if 0.05*deb >= 11:
        return True
    else:
        return False

#q3
def capMin(nb_annees,but):
    i = 1
    while i < nb_annees:
        but = (but + 11) / 1.05
        i += 1
    return but

#q4
def dureeMin(capital,but):
    a = 0
    if capital > 220:
        while capital < but:
            capital = (capital * 1.05) - 11
            a +=1
        print(a)
    else:
        print("-1")

nba = int(input("nombre d'années d'investissement :"))
deb = int(input("capital initial :"))
nb_annees = int(input("nombre d'années investies :"))
but = int(input("Objectif de capital :"))
print(capital(nba, deb))
print(gagne(nba, deb))
print(capMin(nb_annees, but))
print(dureeMin(capital, but))

#  Un peu d’arithmétique :
#q1
def plus_grand_diviseur_premier(n):
    a = 1
    while a >= n:
        if est_premier(n):
            return n
        elif est_premier(a):
            if a%n == 0:
                div_max = a
    return div_max

#q2
def pgcd(a,b):
    if a < b:
        c = a
        a = b
        b = c
    elif a == b:
        return a
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
    return b

#q3
def ppcm(a,b):
    if a < b:
        c = a
        a = b
        b = c
    i = a
    while i > 0:
        if a%i and b%i:
            ppm = i
    return ppm

#q4
def irreductible(numerateur, denominateur):
    if pgcd(numerateur, denominateur) != 1:
        return True
    else :
        return False

# Suite de Fibonacci :
#q1
def afficher_nthermes_fibo(n):
    i = 1
    f0 = 1
    f1 = 1
    print("F(0) = 1")
    print("F(1) = 1")
    while i <= n:
        fn = f0 + f1
        print("F(", i, ") =", fn)
        f0 = f1
        f1 = fn

#q2
def afficher_niemetherme_fibo(n):
    i = 1
    f0 = 1
    f1 = 1
    while i <= n:
        fn = f0 + f1
        f0 = f1
        f1 = fn
    print("F(", i, ") =", fn)

#q4
def nieme_estimation_nbor(n):
    i = 1
    f0 = 1
    f1 = 1
    fn = 0
    while i <= n:
        fn = f0 + f1
        f0 = f1
        f1 = fn
    print("estimation nombre d'or :", fn/f1)

#q5
def n_pour_nbor(precision):
    i = 1
    f0 = 1
    f1 = 1
    fn = 0
    while abs(scipy.constants.golden - (fn/f1)) > precision:
        fn = f0 + f1
        f0 = f1
        f1 = fn
    return i

# Suite de Syracuse :
#q1
def calcul_vol(a):
    un = a
    i = 0
    while un == 1:
        if un%2 == 0:
            un /= 2
        else:
            un = (un*3) + 1
        i += 1
    return i

#q2
# print("durée de vol avec A :", calcul_vol(int(input("A = "))))

#q3
# play = True
# while play:
#     print("durée de vol avec A :", calcul_vol(int(input("A = "))))
#     replay = int(input("rejouer ?"))
#     if replay != "oui":
#         play = False

#q4
def trouver_A_long(b):
    a = 1
    vol_max = 1
    while a < b:
        un = a
        i = 0
        while un == 1:
            if un%2 == 0:
                un /= 2
            else:
                un = (un*3) + 1
            i += 1
        if i > vol_max:
            vol_max = i
        a += 1
    return vol_max

# q5
def afficher_A_jusquax(x):
    a = 1
    vol_max = 1
    while a < x:
        un = a
        i = 0
        while un == 1:
            if un%2 == 0:
                un /= 2
            else:
                un = (un*3) + 1
            i += 1
        a += 1
        print("pour A = ", a, "la distance de vol est :", i)

# question 6 correspond a la question 4, ou incomprehension...