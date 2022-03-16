from enum import Enum
from random import randint

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

def genererGrilleEtBombes(largeur: int, hauteur: int, nbBombes: int):
    # Génère la grille de jeu et place les bombes.

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

        # Si il n'y a pas déjà une bombe, placer une bombe et décrémenter le variant de boucle nbBombes qui repr�sente le nombre de bombes restantes à placer.
        if not bombes[colonne][ligne]:
            bombes[colonne][ligne] = True
            nbBombes -= 1

    return grille, bombes

def compterBombesVoisines(colonne: int, ligne: int, bombes):
    largeur = len(bombes)-1
    hauteur = len(bombes[0])-1
    bombesVoisines = 0
    for i in range(colonne - 1 if colonne > 0 else 0,
                   colonne + 2 if colonne < largeur else largeur):
        for j in range(ligne - 1 if ligne > 0 else 0,
                       ligne + 2 if ligne < hauteur else hauteur):
            if bombes[i][j]:
                bombesVoisines += 1
    return bombesVoisines

# Chemin du dossier des textures relatif au répertoire racine de l'application.
CHEMIN_DOSSIER_TEXTURES = ".\\model\\textures\\"

# Côté en pixels des cases et de leur textures associées.
COTE_CASE = 32

