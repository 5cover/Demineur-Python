from enum import Enum
from random import randint

class case(Enum):
    """ Les diff�rentes cases possibles et les noms de fichier de leur textures"""
    PLEINE = "pleine.png"
    """ Case pleine pouvant cacher une bombe """
    VIDE = "vide.png"
    """ Case creus�e par le joueur """
    DRAPEAU = "drapeau.png"
    """ Case contenant un drapeau pla�� par le joueur, marquant ou non l'emplacememnt d'une bombe. Un chiffre de 0 � 8 s'affiche dessus selon le nombre de cases voisines contenant une bombe. """
    EXPLOSEE = "explosee.png"
    """ Case contenant une bombe explos�e """

def genererGrilleEtBombes(hauteur: int, largeur: int, nbBombes: int):
    # G�nere la grille de jeu et place les bombes.

    if hauteur < 0 or largeur < 0:
        raise ValueError("La hauteur et la largeur doivent �tre positives.")
    if nbBombes < 0 or nbBombes > hauteur * largeur:
        raise ValueError("Le nombre de bombes doit se trouver entre 0 et le nombre total de cases.")
        
    grille = [[Case.Vide()] * hauteur for _ in range(largeur)]
    bombes = [[False] * hauteur for _ in range(largeur)]

    while nbBombes > 0:
        # Choisir un emplacement al�atoire sur la grille
        ligne = randint(0, hauteur-1)
        colonne = randint(0, largeur-1)

        # Si il n'y a pas d�j� une bombe, placer une bombe et d�cr�menter le variant de boucle nbBombes qui repr�sente le nombre de bombes restantes � placer.
        if not bombes[ligne][colonne]):
            bombes[ligne][colonne] = True
            nbBombes -= 1

    return grille, bombes

# Chemin du dossier des textures relatif au r�pertoire racine de l'application.
CHEMIN_DOSSIER_TEXTURES = "model\textures\"

