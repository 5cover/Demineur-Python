import controller.config as config
import view.interface as interface
from controller.config import largeurGrille, hauteurGrille, soustractionIndexSure, additionIndexSure, verifierSiPartieGagnee

_premierClicGauche = True
_partiePerdue = False

def caseClic(c: int, l: int, buttonNumber: int):
    global _premierClicGauche, _partiePerdue

    if buttonNumber == 1 and not _partiePerdue:
        if _premierClicGauche:
            _premierClicGauche = False
            config.placerBombes(c, l)
            creuserZoneExclusion(c, l)
        caseClicGauche(c, l)
    elif buttonNumber == 2:
        _partiePerdue = False
        _premierClicGauche = True
        interface.nouvellePartie()
        return
    elif buttonNumber == 3 and not _partiePerdue:
        caseClicDroit(c, l)

    if config.verifierSiPartieGagnee():
        interface.partieGagnee()

def caseClicGauche(c: int, l: int):
    """ Réponse à un clic gauche sur une case """
    # La case cliquée contient une bombe et l'utilisateur n'a pas placé de drapeau dessus
    if config.bombes[c][l] and config.grille[c][l] != config.case.DRAPEAU:
        perdre()
    # La case cliquée est une case pleine qui ne contient pas de bombe.
    elif config.grille[c][l] == config.case.PLEINE:
        creuser(c, l)


def caseClicDroit(c: int, l: int):
    """ Réponde à une clic droit sur une case """

    # L'utilisateur souhaite placer un drapeau sur la case
    if config.grille[c][l] == config.case.PLEINE:
        placerDrapeau(c, l)

    # L'utilisateur souhaite enlever le drapeau de la case
    elif config.grille[c][l] == config.case.DRAPEAU:
        enleverDrapeau(c, l)

def creuserZoneExclusion(ccze, lcze):
    rayonLarge = int(largeurGrille() * config.MULTIPLICATEUR_ZONE_EXCLUSION / 2)
    rayonHaut = int(hauteurGrille() * config.MULTIPLICATEUR_ZONE_EXCLUSION / 2)

    for c in range(soustractionIndexSure(ccze, rayonLarge), additionIndexSure(ccze, rayonLarge+1, largeurGrille())):
        for l in range(soustractionIndexSure(lcze, rayonHaut), additionIndexSure(lcze, rayonHaut+1, hauteurGrille())):
            creuser(c, l)

def creuser(c, l):
    config.grille[c][l] = config.case.VIDE
    
def placerDrapeau(c, l):
    config.grille[c][l] = config.case.DRAPEAU
    
def enleverDrapeau(c, l):
    config.grille[c][l] = config.case.PLEINE

def perdre():
    global _partiePerdue
    _partiePerdue = True
    interface.partiePerdue()
    """ Perdre la partie et révéler toutes les bombes. """
    for ligne in range(largeurGrille()):
        for colonne in range (hauteurGrille()):
            if config.bombes[ligne][colonne]:
                config.grille[ligne][colonne] = config.case.EXPLOSEE
