from copy import *
# recherche dans une liste

#minimums
def minimum(li):
    mini = li[0]
    for e in li:
        if e < mini:
            mini = e
    return mini

def contient(li, elem):
    i = 0
    while i < len(li):
        if li[i] == elem:
            return True
        i += 1
    return False

def min_plus_grand_que(li, x):
    for e in li:
        if (e-x)>=0:
            mini = e
            for e in li:
                if e < mini and (e-x)>=0:
                    mini = e
            return mini
    return None

def minimum2(li):
    return min_plus_grand_que(li,minimum(li))

def minimum3(li):
    x = minimum(li)
    for e in li:
        if (e-x)>0:
            mini = e
            for e in li:
                if e < mini and (e-x)>0:
                    mini = e
            return mini
    return None

# temperatures

def proche_zero(lt):
    if lt == []:
        return 0
    mini = lt[0]
    for e in lt:
        if abs(e) < abs(mini) or (mini < 0 and mini == (-e)):
            mini = e
    return mini

# modification listes

def moyenne():
    n = int(input("nombre strictement positif : "))
    i = 0
    m = 0
    while n < 0:
        m += n
        n = int(input("nombre strictement positif : "))
        i += 1
    return m/i

def inversion(l):
    l_inverse = []
    for e in l:
        l_inverse.insert(0,e)
    return l_inverse

# duels de chevaux

#force des chevaux
def plus_proches(li):
    diff_min = abs(li[0] - li[1])
    for e1 in range(len(li)):
        for e2 in range(e1+1, len(li)):
            if abs(li[e1] - li[e2]) < diff_min:
                diff_min = abs(li[e1] - li[e2])
    return diff_min

def plus_proches_et_numero(li):
    diff_min = abs(li[0] - li[1])
    num1 = 0
    num2 = 1
    for e1 in range(len(li)):
        for e2 in range(e1+1, len(li)):
            if abs(li[e1] - li[e2]) < diff_min:
                diff_min = abs(li[e1] - li[e2])
                num1 = e1
                num2 = e2
    return diff_min, num1, num2

# le retour des courses

def couples_chevaux(li):
    liste_couples = []
    dtotal = 0
    while li != []:
        d, n1, n2 = plus_proches_et_numero(li)
        couple = [li[n1], li[n2]]
        liste_couples.append(couple)
        if n1 < n2:
            del li[n1]
            del li[n2-1]
        else:
            del li[n1]
            del li[n2+1]
        dtotal += d
    return liste_couples, d

def couples_chevaux_overkill(li):
    meilleure_liste = []
    liste_de_base = deepcopy(li)
    def couples_overkill(li, n1, n2):
        liste_couples = []
        dtotal = 0
        while li != []:
            d = abs(li[n1] - li[n2]) # beug car la liste ne redeviens pas l'initiale
            couple = [li[n1], li[n2]]
            liste_couples.append(couple)
            if n1 < n2:
                del li[n1]
                del li[n2-1]
            else:
                del li[n1]
                del li[n2+1]
            dtotal += d
        return liste_couples, dtotal
    for n1 in range(len(liste_de_base)):
        for n2 in range(n1+1, len(liste_de_base)):
            liste_couples, dtotal = couples_overkill(li, n1, n2)
            liste_et_d = [liste_couples, dtotal]
            print("etape :", n1, n2,"liste et d :", liste_et_d)
            meilleure_liste.append(liste_et_d)
            li = deepcopy(liste_de_base)
    return meilleure_liste



# liste = [5, 15, 17, 3, 8, 11, 28, 6, 55, 7]
# liste2 = [12, 13, 11, 15]
# print(couples_chevaux(liste2))
# print(couples_chevaux_overkill(liste))

# liste de mots

def mot_le_plus_long(texte):
    liste_mots = texte.split()
    maxi = liste_mots[0]
    for e in liste_mots:
        if len(e) > len(maxi):
            maxi = e
    return maxi

def mot_plus_long_que_moyenne(texte):
    liste_mots = texte.split()
    m = 0
    for e in liste_mots:
        m += len(e)
    m /= len(liste_mots)
    for e in liste_mots:
        if len(e) > m:
            print(e)

def nb_voyelles(mot):
    v = ["a","e","i","o","u","y"]
    nbv = 0
    liste_lettres = mot.split() # marche pas
    for e in liste_lettres:
        if e in v:
            nbv += 1
    return nbv

def mot_plus_de_voyelles(texte):
    liste_mots = texte.split()
    maxi = nb_voyelles(liste_mots[0])
    for e in liste_mots:
        if nb_voyelles(e) > nb_voyelles(maxi):
            maxi = e
    return maxi

# texte = "il etait une fois dans une foret abandonnée"
# print(mot_plus_de_voyelles(texte))
