from enum import Enum
from random import randrange, choice

CHEMIN_DOSSIER_TEXTURES = ".\\model\\textures\\"
""" Chemin du dossier des textures relatif au répertoire racine de l'application. """

COTE_CASE = 32
""" Côté en pixels des cases et de leur textures associées. """

RAYON_BOMBE = 1
""" Rayon de recherche de bombes voisines. """

MULTIPLICATEUR_ZONE_EXCLUSION = 1/3
""" Ratio entre les dimensions de la grille et celles de la zone d'exclusion sans bombe autour de la première case creusée. """

grille = None
bombes = None
nbBombes = 0

class case(Enum):
    """ Les différentes cases possibles et les noms de fichier de leur textures"""
    PLEINE = "pleine.gif"
    """ Case pleine pouvant cacher une bombe """
    VIDE = "vide.gif"
    """ Case creusée par le joueur """
    DRAPEAU = "drapeau.gif"
    """ Case contenant un drapeau placé par le joueur, marquant ou non l'emplacement d'une bombe. Un chiffre de 0 à 8 s'affiche dessus selon le nombre de cases voisines contenant une bombe. """
    EXPLOSEE = "explosee.gif"
    """ Case contenant une bombe explosée """

def genererGrille(largeur: int, hauteur: int, nombreBombes: int):
    """ Génère la grille de jeu et dissémine les bombes. """

    global grille, bombes, nbBombes

    nbBombes = nombreBombes

    if hauteur < 1 or largeur < 1:
        raise ValueError("La hauteur et la largeur doivent être supérieures ou égales à 1.")
    if nbBombes < 0 or nbBombes > largeur * hauteur:
        raise ValueError("Le nombre de bombes doit se trouver entre 0 et le nombre total de cases.")
    
    grille = [[case.PLEINE] * hauteur for _ in range(largeur)]
    bombes = [[False] * hauteur for _ in range(largeur)]

def placerBombes(c, l):
    """ Place les bombes. Les bombes ne sont placées que sur les cases pleines."""
    bombesRestantes = nbBombes
    # colonne ∈ [ 0 ; c-rayonLarge [ ∪ ] c+rayonLarge ; largeurGrille() [

    # ligne   ∈ [ 0 ; l-rayonHaut  [ ∪ ] l+rayonHaut  ; hauteurGrille() [

    while bombesRestantes > 0:
        # Choix d'un emplacement aléatoire sur la grille
        ligne = randrange(0, largeurGrille())
        colonne = randrange(0, hauteurGrille())

        # Si il n'y a pas déjà une bombe et que l'empalcememt choisi est en dehors de la zone d'exclusion,
        # placer une bombe et décrémenter le variant de boucle nbBombes qui représente le nombre de bombes restantes à placer.
        if not pointAppartientAZoneExlusion(colonne, ligne, c, l) and not bombes[colonne][ligne]:
            bombes[colonne][ligne] = True
            bombesRestantes -= 1

def pointAppartientAZoneExlusion(c, l, colonneCentraleZoneExclusion, ligneCentraleZoneExclusion):
        rayonLarge = int(largeurGrille() * MULTIPLICATEUR_ZONE_EXCLUSION / 2)
        rayonHaut = int(hauteurGrille() * MULTIPLICATEUR_ZONE_EXCLUSION / 2)

        return c >= colonneCentraleZoneExclusion-rayonLarge and c <= colonneCentraleZoneExclusion+rayonLarge and l >= ligneCentraleZoneExclusion-rayonHaut and l <= ligneCentraleZoneExclusion+rayonHaut

def additionIndexSure(i, x, maxi):
    """ Addition d'un index à un nombre sans dépasser un maximum donné. """
    if i + x >= maxi:
        return maxi-1
    return i + x

def soustractionIndexSure(i, x):
    """ Soustraction d'un nombre à un index sans dépassser 0. """
    if i - x < 0:
        return 0
    return i - x

def verifierSiPartieGagnee():
    """ Vérifie si tous les drapeaux se trouvent sous toutes les bombes"""
    for c in range(largeurGrille()):
        for l in range(hauteurGrille()):
            # Si on trouve un drapeau sans bombe ou une bombe sans drapeau
            if (grille[c][l]==case.DRAPEAU) ^ bombes[c][l]: # ^ correspond à un OU Exclusif (XOR)
                return False
    return True

def largeurGrille():
    return len(grille)
def hauteurGrille():
    return len(grille[0])

def compterBombesVoisines(c: int, l: int,):
    """ Compte le nombre de bombes dans les cases voisines d'une case. """

    bombesVoisines = 0

    for i in range(c-RAYON_BOMBE if c>RAYON_BOMBE else 0,
                   c+RAYON_BOMBE+1 if c+RAYON_BOMBE<largeurGrille() else largeurGrille()):
        for j in range(l-RAYON_BOMBE if l>RAYON_BOMBE else 0,
                       l+RAYON_BOMBE+1 if l+RAYON_BOMBE<hauteurGrille() else hauteurGrille()):
                if bombes[i][j]:
                    bombesVoisines += 1

    # Dans le cas où il y a une bombe à l'emplacement passé à la fonction, on diminue de 1, car ne souhaite pas compter les bombes sur la case.
    if bombes[c][l]:
        bombesVoisines -= 1
        
    return bombesVoisines

def choisirCouleur(n: int):
    """ Choisit la couleur à utiliser selon le nombre de bombes voisines.
    Si la valeur passée ne correspond à aucune couleur, retourne noir ("black").
    Les couleurs sont basées sur le jeu de Démineur original. """
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
