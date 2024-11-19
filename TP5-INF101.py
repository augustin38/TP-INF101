# le journal de Mr Bizzare :

def lundi(mot):
    return mot + " " + mot

def mardi(mot):
    if len(mot)%2 == 0:
        return (mot + "-")*5 + mot
    else:
        return (mot + ",")*2 + mot
    
def mercredi(mot):
    if len(mot)%2 != 0:
        return "impair"
    else:
        return mot

def jeudi(mot):
    return mot*(len(mot)%3)

def vendredi(mot):
    if "A" <= mot[0] <= "Z":
        result = ""
        for i in range(1, len(mot)):
            result += mot[i]
        return result
    elif "a" <= mot[0] <= "z":
        result = ""
        for i in range(0, len(mot)-1):
            result += mot[i]
        return result

def samedi(mot):
    i = 1
    print("test")
    inverse = ""
    while i <= len(mot):
        inverse += mot[-i]
        i += 1
    return inverse

def dimanche(mot):
    i = 0
    espace = ""
    while i < (len(mot)-1):
        espace += (mot[i] + " ")
        i += 1
    return espace + mot[-1]

def transforme(mot, num_jour):
    if num_jour == 1:
        return lundi(mot)
    elif num_jour == 2:
        return mardi(mot)
    elif num_jour == 3:
        return mercredi(mot)
    elif num_jour == 4:
        return jeudi(mot)
    elif num_jour == 5:
        return vendredi(mot)
    elif num_jour == 6:
        return samedi(mot)
    elif num_jour == 7:
        return dimanche(mot)
    else:
        print("erreur")
        return ""

# Chiffrement de texte :

# Chiffrement de césar :

def code_cesar(mot):
    i = 0
    if mot.islower():
        mot = mot.upper()
    cesar = ""
    while i < len(mot):
        if ord(mot[i]) <= 87:
            cesar += chr((ord(mot[i])+3))
        elif ord(mot[i]) > 87:
            cesar += chr((ord(mot[i])-23))
        i += 1
    return cesar

def texte_cesar(texte):
    texte_cesar = ""
    i = 0
    while i < len(texte):
        mot = ""
        while i < len(texte) and texte[i] != " ":
            mot += texte[i]
            i += 1
        texte_cesar += (code_cesar(mot) + " ")
        i += 1
    return texte_cesar

# Chiffrement numerique :
def code_ord(mot):
    ordre = ""
    for l in range(len(mot)-1):
        if mot[l].islower():
            ordre += (str(ord(mot[l])-96) + "+")
        elif mot[l].isupper():
            ordre += (str(ord(mot[l])-64) + "+")
    if mot[l].islower():
        ordre += str(ord(mot[-1])-96)
    elif mot[l].isupper():
        ordre += str(ord(mot[-1])-64)
    return ordre

def texte_ord(texte):
    texte_ord = ""
    i = 0
    while i < len(texte):
        mot = ""
        while i < len(texte) and texte[i] != " ":
            mot += texte[i]
            i += 1
        texte_ord += (code_ord(mot) + " ")
        i += 1
    return texte_ord

# programme principal :
# retry = "oui"
# while retry == "oui":
#     ty = int(input("1-Chiffrement césar \n2-Chiffrement numérique \nchoisissez : "))
#     texte = input("Un texte a coder : ")
#     if ty == 1:
#         print("texte codé : ", texte_cesar(texte))
#         retry = input("voulez vous reessayer (oui / non) ?")
#     elif ty == 2:
#         print("texte codé : ", texte_ord(texte))
#         retry = input("voulez vous reessayer (oui / non) ?")
#     else:
#         print("erreur, reessayez :")

# Jeu du pendu :

def lettre_deja_joue(l,liste_lettres):
    if l in liste_lettres:
        return False
    else:
        liste_lettres += l
        return True, liste_lettres

def lettre_combien(l,mot,liste_lettres):
    i = 0
    print("devine mon mot : ", end ="")
    for lettre in mot:
        if lettre == l or lettre in liste_lettres:
            if lettre == l:
                i += 1
                print(l, " ", sep ="", end = "")
            elif lettre in liste_lettres:
                print(lettre, end = "")
        else:
            print("_ ",end = "")
    if i >= 1:
        print("\nIl y a",i ,l)
    else:
        print("\nIl n'y a pas de", l)

def erreur(l,e,mot,liste_erreurs):
    if l not in mot:
        liste_erreurs += l
        return (e-1), liste_erreurs
    else:
        return e, liste_erreurs

def partie_gagnee(mot,liste_lettres):
    lettres_trouves = 0
    for a in mot:
        if a in liste_lettres:
            lettres_trouves += 1
    if lettres_trouves == len(mot):
        return True


play = "oui"
while play == "oui":
    mot = input("Mot secret :")
    e = int(input("Nombre d'erreurs autorisées :"))
    print("Devine mon mot :", len(mot)*" _")
    print("Tu a le droit a", e, "erreurs")
    liste_lettres = ""
    liste_erreurs = ""
    win = False
    while e > 0 and not(win):
        l = input("")
        verif, liste_lettres = lettre_deja_joue(l,liste_lettres)
        win = partie_gagnee(mot, liste_lettres)
        if win:
            play = input("Vous avez gagné ! reassayer (oui/non) ?")
        elif verif:
            e, liste_erreurs = erreur(l,e,mot,liste_erreurs)
            lettre_combien(l,mot,liste_lettres)
            print("Tu a le droit a", e, "erreurs")
        else:
            print("lettre deja jouée, réessayez \n")
    if e == 0:
        play = input("Vous avez perdu, reassayer (oui/non) ?")
