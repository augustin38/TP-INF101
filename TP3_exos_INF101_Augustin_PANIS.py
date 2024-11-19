from turtle import *
from math import *
setup(1000, 1000)

# # Marchons au pas de Turtle :

# # Carré :
# c=1
# while c<=4:
#     forward(100)
#     right(90)
#     c+=1

# # Carré bis :
# c=1
# up()
# goto(-50, 20)
# down()
# while c<=4:
#     forward(100)
#     right(90)
#     c+=1

# # Triangle equilatéral :
# c=1
# while c<=3:
#     forward(100)
#     right(120)
#     c+=1

# # Ligne de carrés :
# i = 0
# up()
# goto(-200, 200)
# down()
# while i <= 8:
#     c=1
#     while c<=4:
#         forward(50)
#         right(90)
#         c+=1
#     up()
#     forward(60)
#     down()
#     i+=1

# # Pavage de carrés :
# j = 0
# up()
# goto(-200, 200)
# down()
# while j <= 4:
#     i = 0
#     while i <= 8:
#         c=1
#         while c<=4:
#             forward(50)
#             right(90)
#             c+=1
#         up()
#         forward(60)
#         down()
#         i+=1
#     j+=1
#     up()
#     goto(-200, (200-60*j))
#     down()

# # Ligne de carrés et de triangles alternés :
# i = 0
# up()
# goto(-200, 200)
# down()
# n = int(input("Combien de figures :"))
# while i <= n:
#     if i %2 == 0:
#         c=1
#         while c<=4:
#             forward(50)
#             right(90)
#             c+=1
#         up()
#         forward(60)
#         down()
#         i+=1
#     else:
#         t=0
#         while t<=3:
#             forward(50)
#             right(120)
#             t +=1
#         up()
#         forward(60)
#         down()
#         i+=1

# A la découverte des fonctions à travers le dessin :

# # Programme mystère :
# import turtle
# i = 0
# while i < 360 :
#     turtle.forward(2)
#     turtle.left(1)
#     i=i+1
# turtle.circle(115)

# # Une première fonction :
# import turtle
# def carre() :
#     i = 1 
#     while i <= 4 :
#         turtle.forward(100)
#         turtle.right(90)
#         i = i + 1

# carre()
# turtle.up()
# turtle.forward(130)
# turtle.down()
# carre()

# Fonction carre avec paramètre :
def  carre(cote) :
    i = 1
    while i <= 4 :
        forward(cote)
        right(90)
        i +=1
def  carre_p(x,y,cote) :
    i = 1
    up()
    goto(x, y)
    down()
    while i <= 4 :
        forward(cote)
        right(90)
        i +=1

# Fonction pour tracer un triangle équilatéral :
def triangle(cote) :
    i = 1
    while i <= 3 :
        forward(cote)
        right(120)
        i +=1
def triangle_p(x,y,cote) :
    i = 1
    up()
    goto(x, y)
    down()
    while i <= 3 :
        forward(cote)
        right(120)
        i +=1

# # Ligne de carrés et triangles avec fonctions :
# i = 0
# up()
# goto(-200, 200)
# down()
# n = int(input("Combien de figures :"))
# while i <= n:
#     if i %2 == 0:
#         carre(50) # fonction carre
#         up()
#         forward(60)
#         down()
#         i+=1
#     else:
#         triangle(50) # fonction triangle
#         up()
#         forward(60)
#         down()
#         i+=1

# # Pour aller plus loin :

# # Ligne de carrés et triangles alternés de tailles croissantes :
# i = 0
# up()
# goto(-200, 200)
# down()
# d = 40
# n = int(input("Combien de figures :"))
# while i <= n:
#     if i %2 == 0:
#         carre(d) # fonction carre
#         up()
#         forward(d+10)
#         down()
#         i+=1
#     else:
#         triangle(d) # fonction triangle
#         up()
#         forward(d+10)
#         down()
#         i+=1
#     d+= 15

# Rosace et pavage de rosaces :
def rosace(x, y, nb, r):
    up()
    goto(x, y)
    down()
    i = 1
    while i <= nb:
        circle(r)
        right(360/nb)
        i+= 1

# rosace(0, 0, 4, 30)

def lrosaces(x, y, nb, r, tl):
    i = 1
    while i <= tl:
        rosace(x, y, nb, r)
        x += ((4*r)+10)
        i+=1

# lrosaces(0, 0, 4, 30, 2)

def crosaces(x, y, nb, r, tl, tp):
    i = 1
    while i <= tp:
        lrosaces(x, y, nb, r, tl)
        y -= ((4*r)+10)
        i+=1

# crosaces(0, 0, 4, 30, 2, 3)

# Figures imbriquées :

# Carrés imbriqués :
def carres_imbriques(cote_debut, nb_carres):
    i = 1
    while i <= nb_carres:
        carre(cote_debut)
        cote_debut = cote_debut * (2/3)
        i+=1

# carres_imbriques(100, 9)

# Se déplacer (1):
def aller_sans_tracer(x,y):
    up()
    goto(x, y)
    down()

# Se déplacer (2):
def descendre_sans_tracer(longueur):
    up()
    right(90)
    forward(longueur)
    left(90)
    down()

# Polygone (1):
def polygone(nb_cotes,cote):
    i = 1
    while i <= nb_cotes :
        forward(cote)
        right(360/nb_cotes)
        i +=1

# polygone(6, 60)

# Polygone (2):
def diametre_polygone(nb_cotes, cote):
    d = (cote)/sin(pi/nb_cotes)
    return d

# print(diametre_polygone(8, 40))

# Pavage de polygones (1):
def colonne_polygone(nb_poly, cote):
    i = 1
    n_cote = 3
    while i <= nb_poly:
        polygone(n_cote, cote)
        n_cote += 1
        descendre_sans_tracer((5 + diametre_polygone(n_cote, cote)))
        i += 1
    return n_cote

# colonne_polygone(10, 20)

# Pavage de polygones (2):
def pavage(nb_poly, nb_col, cote):
    up()
    x = -270
    y = 330
    goto(x, y)
    down()
    i = 1
    while i <= nb_col:
        n_cote = colonne_polygone(nb_poly, cote)
        up()
        x = x +(10 + diametre_polygone(n_cote, cote))
        goto(x, y)
        down()
        cote += 10
        i += 1

# pavage(5, 3, 30)

# Pavage de polygones (3):
pavage(3, 3, 20)
carres_imbriques(100, 5)
