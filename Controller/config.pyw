from enum import Enum
from random import randint

class case(Enum):
    """ Les différentes cases possibles et les noms de fichier de leur textures"""
    PLEINE = "pleine.png"
    """ Case pleine pouvant cacher une bombe """
    VIDE = "vide.png"
    """ Case creusée par le joueur """
    DRAPEAU = "drapeau.png"
    """ Case contenant un drapeau plaçé par le joueur, marquant ou non l'emplacememnt d'une bombe. Un chiffre de 0 à 8 s'affiche dessus selon le nombre de cases voisines contenant une bombe. """
    EXPLOSEE = "explosee.png"
    """ Case contenant une bombe explosée """

def genererGrilleEtBombes(hauteur: int, largeur: int, nbBombes: int):
    # Génere la grille de jeu et place les bombes.

    if hauteur < 0 or largeur < 0:
        raise ValueError("La hauteur et la largeur doivent être positives.")
    if nbBombes < 0 or nbBombes > hauteur * largeur:
        raise ValueError("Le nombre de bombes doit se trouver entre 0 et le nombre total de cases.")
        
    grille = [[Case.Vide()] * hauteur for _ in range(largeur)]
    bombes = [[False] * hauteur for _ in range(largeur)]

    while nbBombes > 0:
        # Choisir un emplacement aléatoire sur la grille
        ligne = randint(0, hauteur-1)
        colonne = randint(0, largeur-1)

        # Si il n'y a pas déjà une bombe, placer une bombe et décrémenter le variant de boucle nbBombes qui représente le nombre de bombes restantes à placer.
        if not bombes[ligne][colonne]):
            bombes[ligne][colonne] = True
            nbBombes -= 1

    return grille, bombes

# Chemin du dossier des textures relatif au répertoire racine de l'application.
CHEMIN_DOSSIER_TEXTURES = "model\textures\"

