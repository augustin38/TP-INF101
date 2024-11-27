from random import *
# Jeu du démineur

# structure de données
def creerGrille(N, M, v = 0):
    ligne = []
    for m in range(M):
        ligne.append(v)
    liste = []
    for n in range(N):
        liste.append(ligne)
    return liste

def placerMines(grille, X):
    for e in range(X):
        i = randint(0, (len(grille)-1))
        j = randint(0, (len(grille[0])-1))
        while grille[i][j] == 1:
            i = randint(0, (len(grille)-1))
            j = randint(0, (len(grille[0])-1))
        grille[i][j] = 1

# Compter les mines
def testMine(grille, i, j):
    if grille[i][j] == 1:
        return True
    return False

def compteMinesVoisines(grille, i, j):
    compteur = 0
    for e1 in [0, -1, 1]:
        for e2 in [0, -1, 1]:
            it = i + e1
            jt = j + e2
            if not(e1 == e2 == 0) and 0 <= it < len(grille) and 0 <= jt < len(grille[0]):
                compteur += 1
    return compteur

# Affichage
def afficheSolution(grille):
    for i in range(len(grille)):
        for j in grille[i]:
            if j == 0:
                print("-", end="")
            elif j == 1:
                print("*", end="")
        print("")

def afficheJeu(grille, casesDevoilees):
    for i in casesDevoilees:
        for j in casesDevoilees[i]:
            if casesDevoilees[i][j]:
                if grille[i][j] == 0:
                    print(compteMinesVoisines(grille, i, j), end="")
                elif grille[i][j] == 1:
                    print("*", end="")
            else:
                print("?", end="")
        print("")

# Interaction avec le joueur
def getNbMines(N, M):
    X = int(input("Nombre de mines : "))
    while not(1 <= X  < (N*M)):
        X = int(input("Nombre de mines incorrect, recommencez : "))
    return X

def getCoords(casesDevoilees, N, M):
    print("A toi de jouer :")
    ligne = int(input("Ligne ? "))
    while 0 <= ligne < N:
        ligne = int(input("Ligne <", N, "svp ? "))
    colonne = int(input("Colonne ? "))
    while 0 <= ligne < M:
        ligne = int(input("Colonne <", M, "svp ? "))
    if casesDevoilees[ligne][colonne] != "?":
        while casesDevoilees[ligne][colonne] != "?":
            print("Case deja devoilée, recommence :")
            ligne = int(input("Ligne ? "))
            while 0 <= ligne < N:
                ligne = int(input("Ligne <", N, "svp ? "))
            colonne = int(input("Colonne ? "))
            while 0 <= ligne < M:
                ligne = int(input("Colonne <", M, "svp ? "))
    return ligne, colonne

# Programme principal :
N = int(input("Nombre de lignes : "))
M = int(input("Nombre de Colonnes : "))
grille = creerGrille(N, M)
X = getNbMines(N, M)
placerMines(grille, X)
casesDevoilees = [[False for a in range(M)] for b in range(N)]
coup = 1
nb_inconnues = len(grille)*len(grille[0])

i, j = getCoords(casesDevoilees, N, M)
while testMine(grille, i, j) and (nb_inconnues - X) > 0:
    print("Coup numero", coup)
    afficheJeu(grille, casesDevoilees)
    i, j = getCoords(casesDevoilees, N, M)
    coup += 1

if testMine(grille, i, j):
    print("Tu a gagné en", coup, "coups, bravo !")
else:
    print("Perdu, vous avez touché une mine !")
    afficheJeu(grille, casesDevoilees)
    afficheSolution(grille)