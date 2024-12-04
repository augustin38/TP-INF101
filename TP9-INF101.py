from random import *
from turtle import *
import time
# TP9 : algorithmes pour trier des listes
# 1 : Algorithmes de tri
def tri_insertion(liste):
    new_li = []
    li = list(liste)
    while len(li) > 0:
        ind = 0
        for e in range(len(li)):
            if li[e] < li[ind]:
                ind = e
        new_li.append(li[ind])
        li.pop(ind)
    return new_li

def tri_selection(liste):
    for i in range(len(liste)):
        ind = i
        for j in range(i, len(liste)):
            if liste[j] < liste[ind]:
                ind = j
        liste[i], liste[ind] = liste[ind], liste[i]
    return liste


def tri_bulle(liste):
    for e in range(len(liste)):
        for i in range(len(liste)-1):
            if liste[i+1] < liste[i]:
                liste[i+1], liste[i] = liste[i], liste[i+1]
    return liste

def test(n, inf, sup):
    li = []
    for i in range(n):
        li.append(randint(inf, sup))
    return li

# n = int(input("taille de la liste a trier : "))
# inf = int(input("borne inferieure de la liste a trier : "))
# sup = int(input("borne superieure de la liste a trier : "))
# print(tri_insertion(test(n, inf, sup)))
# print(tri_selection(test(n, inf, sup)))
# print(tri_bulle(test(n, inf, sup)))

# 2 : Course à pied
def creation_li():
    li = []
    for a in range(365):
        li.append(randint(0, 10000)/100)
    return li

# print(creation_li())

def moy_j(li, j):
    nb = 0 ; moy = 0
    for e in range(0, len(li), j):
        moy += li[e]
        nb += 1
    return moy/nb

# print(moy_j(creation_li(), 3))

def moy_année(li):
    lim = []
    for a in range(1, 8):
        lim.append(moy_j(li, a))
    return lim

# print(moy_année(creation_li()))

def affiche_moy_turtle(li):
    goto(0, 100)
    goto(0,0)
    goto(365, 0)
    goto(0,0)
    lim = moy_année(li)
    for e in range(len(lim)):
        goto(e*(365/7), lim[e])
    done()
    
# affiche_moy_turtle(creation_li())

# 4 : Comparaison des algorithmes de tri

def tri_insertion_modifié(liste):
    new_li = []
    comp = 0
    ech = 0
    li = list(liste)
    while len(li) > 0:
        ind = 0
        for e in range(len(li)):
            if li[e] < li[ind]:
                comp += 1
                ind = e
        new_li.append(li[ind])
        li.pop(ind)
    return comp, ech

def tri_selection_modifié(liste):
    comp = 0
    ech = 0
    for i in range(len(liste)):
        ind = i
        for j in range(i, len(liste)):
            if liste[j] < liste[ind]:
                comp += 1
                ind = j
        ech += 1
        liste[i], liste[ind] = liste[ind], liste[i]
    return comp, ech


def tri_bulle_modifié(liste):
    comp = 0 ; ech = 0
    for e in range(len(liste)):
        for i in range(len(liste)-1):
            if liste[i+1] < liste[i]:
                liste[i+1], liste[i] = liste[i], liste[i+1]
                ech += 1
            comp += 1
    return comp, ech


# 1) pas fait, bonus
# 2) on peut voir que le tri a bulle met bcp plus de temps a s'executer que les deux autres qui sont très similaires
li = test(1000, 1, 1000)
ti1 = time.time()
compb, echb = tri_bulle_modifié(li)
ti2 = time.time()
compi, echi = tri_insertion_modifié(li)
ti3 = time.time()
comps, echs = tri_selection_modifié(li)
ti4 = time.time()
print("tri bulle : ",ti2 - ti1,"tri insertion : ", ti3 - ti2,"tri selection : ", ti4 - ti3)
# 3)
print("tri bulle : ",compi, echi,"tri insertion : ", comps, echs,"tri selection : ", compb, echb)

# flemme de continuer
