from random import *

# manipulation de dictionnaire français-anglais

def ajouteMot(dfren, mfr, wen):
    dfren[mfr] = wen

def supprimeMot(dico, mot):
    del dico[mot]

def afficheDico(dico):
    for motfr in dico:
        print(motfr, "=", dico[motfr])

def afficheDicoInitiale(dico, lettre):
    print("les mots commencant par", lettre, ":")
    for motfr in dico:
        if motfr[0] == lettre:
            print(motfr, "=", dico[motfr])

def afficheDicoLongueur(dico, longueur):
    print("les mots de longueur", longueur, ":")
    for motfr in dico:
        if len(motfr) == longueur:
            print(motfr, "=", dico[motfr])

fr = {"bonjour" : "hello", "marcher" : "walk", "courir" : "run", "etre" : "be"}

# ajouteMot(fr, "oui", "yes")
# afficheDico(fr)
# supprimeMot(fr, "bonjour")
# afficheDico(fr)
# n = int(input("Longueur des mots : "))
# lettre = input("initiale des mots : ")
# afficheDicoLongueur(fr, n)
# afficheDicoInitiale(fr, lettre)

# mini-jeu de traduction

def traduire(dicofr, mot):
    return dicofr[mot]

def JouerUnMot(dicofr):
    liste_fr = list(dicofr.keys())
    mot = liste_fr[randint(0, len(liste_fr)-1)]
    trad = input(str(mot)+"? ")
    if trad == dicofr[mot]:
        return True, mot
    return False, mot

# print("Jeu de traduction Francais-Anglais :")
# play = True ; score = 0 ; nb_parties = 0
# while play:
#     trouvé, mot = JouerUnMot(fr)
#     if trouvé:
#         print("Correct")
#         score += 1 ; nb_parties += 1
#     else:
#         print("Incorrect, la traduction etait :",fr[mot])
#         nb_parties += 1
#     replay = input("Rejouer ? ")
#     if replay != "oui":
#         play = False
# print("score :", score, "sur", nb_parties)

# multi-joueurs

def trier_scores(dico_scores):
    meilleur_j = "" ; meilleur_score = 0
    for joueur in dico_scores:
        if dico_scores[joueur] > meilleur_score:
            meilleur_score = dico_scores[joueur]
            meilleur_j = joueur
    return meilleur_j, meilleur_score

def affiche_resultats(dico_scores, nb_parties):
    for pos in range(1,4):
        joueur, score = trier_scores(dico_scores)
        del dico_scores[joueur]
        print(pos,". ", joueur, "   ", int((score*100)/nb_parties), "%", sep = "")

# print("Jeu de traduction Francais-Anglais multi joueurs :")
# n_joueurs = int(input("Nombre de joueurs : "))
# nb_parties = int(input("Nombre de parties a jouer : "))
# dico_scores = {}
# for a in range(n_joueurs):
#     dico_scores["joueur "+ str(a)] = 0
# parties = 0

# while parties < nb_parties:
#     for joueur in dico_scores:
#         print("Tour de", joueur)
#         trouvé, mot = JouerUnMot(fr)
#         if trouvé:
#             print("Correct")
#             dico_scores[joueur] += 1
#         else:
#             print("Incorrect, la traduction etait :",fr[mot])
#     parties += 1

# affiche_resultats(dico_scores, nb_parties)

#  traduction de texte

def traduire(txt, fren):
    mots = txt.split()
    for ind in range(len(mots)):
        if mots[ind] in fren:
            mots[ind] = fren[mots[ind]]
        else:
            connaitre = input("traduction de " + str(mots[ind] + " (jsp pour ne pas repondre): "))
            if connaitre != "jsp":
                fren[mots[ind]] = connaitre
                mots[ind] = connaitre
    return " ".join(mots)

texte = input("Texte a traduire :\n")
print(traduire(texte, fr))
print("dictionnaire modifié : ", fr)

#  multi-lingue

# Dictionnaires :

dico_langues = {
"francais" : {
    "hello" : "bonjour",
    "walk" : "marcher",
    "run" : "courir",
    "be" : "être",
    "goodbye" : "au revoir",
    "please" : "s'il vous plaît",
    "thank you" : "merci",
    "yes" : "oui",
    "no" : "non",
    "friend" : "ami"
},
"anglais" : {
    "bonjour" : "hello",
    "marcher" : "walk",
    "courir" : "run",
    "être" : "be",
    "merci" : "thank you",
    "au revoir" : "goodbye",
    "s'il vous plaît" : "please",
    "oui" : "yes",
    "non" : "no",
    "ami" : "friend",
    "maison" : "house",
    "voiture" : "car",
    "chat" : "cat",
    "chien" : "dog",
    "livre" : "book",
    "école" : "school",
    "heure" : "hour",
    "minute" : "minute",
    "jour" : "day",
    "nuit" : "night"
},
"espagnol" : {
    "bonjour" : "hola",
    "marcher" : "caminar",
    "courir" : "correr",
    "être" : "ser",
    "merci" : "gracias",
    "au revoir" : "adiós",
    "s'il vous plaît" : "por favor",
    "oui" : "sí",
    "non" : "no",
    "ami" : "amigo"
}}

def traduction_langue(dico_langues, LG,  LG2, XX):
    print("la traduction de", XX, "de", LG, "vers", LG2, "est", dico_langues[LG2][XX])

mot = input("Choisir un mot :")
print("choisir une langue parmis :", end = "")
for langue in dico_langues:
    print(langue, end = " ")
language = input("langue initiale : ")
language_arrivé = input("langue traduction : ")
traduction_langue(dico_langues, language,  language_arrivé, mot)

mot = input("Choisir un autre mot :")
for langue in dico_langues:
    if langue == "francais":
        language = "anglais"
    else:
        language = "francais"
    traduction_langue(dico_langues, language,  langue, mot)
