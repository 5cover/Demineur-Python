from enum import Enum
from random import randint

CHEMIN_DOSSIER_TEXTURES = ".\\model\\textures\\"
""" Chemin du dossier des textures relatif au répertoire racine de l'application. """

COTE_CASE = 32
""" Côté en pixels des cases et de leur textures associées. """

class case(Enum):
    """ Les différentes cases possibles et les noms de fichier de leur textures"""
    PLEINE = "pleine.gif"
    """ Case pleine pouvant cacher une bombe """
    VIDE = "vide.gif"
    """ Case creusée par le joueur """
    DRAPEAU = "drapeau.gif"
    """ Case contenant un drapeau placé par le joueur, marquant ou non l'emplacememnt d'une bombe. Un chiffre de 0 à 8 s'affiche dessus selon le nombre de cases voisines contenant une bombe. """
    EXPLOSEE = "explosee.gif"
    """ Case contenant une bombe explosée """

def genererGrilleEtBombes(hauteur: int, largeur: int, nbBombes: int):
    """ Génère la grille de jeu et place les bombes. """

    if hauteur < 1 or largeur < 1:
        raise ValueError("La hauteur et la largeur doivent être supérieures ou égales à 1.")
    if nbBombes < 0 or nbBombes > hauteur * largeur:
        raise ValueError("Le nombre de bombes doit se trouver entre 0 et le nombre total de cases.")
    
    grille = [[case.PLEINE] * hauteur for _ in range(largeur)]
    bombes = [[False] * hauteur for _ in range(largeur)]

    while nbBombes > 0:
        # Choisir un emplacement aléatoire sur la grille
        ligne = randint(0, hauteur-1)
        colonne = randint(0, largeur-1)

        # Si il n'y a pas déjà une bombe, placer une bombe et décrémenter le variant de boucle nbBombes qui représente le nombre de bombes restantes à placer.
        if not bombes[colonne][ligne]:
            bombes[colonne][ligne] = True
            nbBombes -= 1

    return grille, bombes

def compterBombesVoisines(ligne: int, colonne: int, bombes):
    """ Compte le nombre de bombes dans les 8 cases voisines d'une case. """
    
    bombesVoisines = 0

    return bombesVoisines

def choisirCouleur(n: int):
    if n == 1:
        return "blue"
    if n == 2:
        return "green"
    if n == 3:
        return "red"
    if n == 4:
        return "indigo"
    if n == 5:
        return "violetred4"
    if n == 6:
        return "turquoise1"
    if n == 7:
        return "black"
    if n == 8:
        return "gray50"

    return "black"