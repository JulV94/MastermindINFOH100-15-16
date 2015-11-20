from random import shuffle
from termcolor import colored, cprint
import sys

def liste_lettre():
    entree = input("\nEntrez la combinaison : ")
    liste_lettres = []
    for letter in entree:
        liste_lettres.append(letter)
    return liste_lettres

def choix_de_la_combinaison():
    lettres_possibles = ['N', 'B', 'J', 'O', 'V', 'R', 'W', 'T']
    shuffle(lettres_possibles)
    combinaison = lettres_possibles[0:4]
    return combinaison
    
def verification_combinaison(combinaison_entree, combinaison):
    verif = True
    for i in range(len(combinaison)):
        if combinaison[i] != combinaison_entree[i]:
            verif*=False
    return verif

def nombre_points_noirs(combinaison_entree, combinaison):       #Bille de la bonne couleur sur la bonne place
    nombre_points_noirs = 0
    for i in range(len(combinaison)):
        if combinaison[i] == combinaison_entree[i]:
            nombre_points_noirs +=1
    return nombre_points_noirs

def nombre_points_blancs(combinaison_entree, combinaison):
    nombre_points_blancs = 0
    for i in range(len(combinaison)):
        if combinaison_entree[i] in combinaison and not(combinaison[i] == combinaison_entree[i]):
            nombre_points_blancs +=1
    return nombre_points_blancs

def affichage_resultat(nbre_blancs, nbre_noirs):
    print("\nNombre de billes de la bonne couleur à la bonne place : ", nbre_noirs)
    print("Nombre de billes de la bonne couleur à la mauvaise place : ", nbre_blancs)

def un_tour_de_jeu(combinaison):
    print("\nCouleurs : Noir = N, Bleu = B, Jaune = J, Orange = O, Vert = V, Rouge = R, Blanc = W, Turquoise = T")
    combinaison_entree = liste_lettre()
    nbre_noirs = nombre_points_noirs(combinaison_entree, combinaison)
    nbre_blancs = nombre_points_blancs(combinaison_entree, combinaison)
    affichage_resultat(nbre_blancs, nbre_noirs)
    return combinaison_entree

def mastermind():
    combinaison = choix_de_la_combinaison()
    #print(combinaison)
    combinaison_entree = 4*[""]
    nombre_tour = 1
    while verification_combinaison(combinaison_entree, combinaison)!= True and nombre_tour <=10:
        print("\nNuméro du tour :", nombre_tour)
        combinaison_entree = un_tour_de_jeu(combinaison)
        nombre_tour += 1
    if verification_combinaison(combinaison_entree, combinaison):
        print("\nVictoire !!!")
    else :
        print("Perdu")
        print("La bonne combinaison était : ", combinaison)

mastermind()
