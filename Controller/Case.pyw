from abc import ABC, abstractmethod # Module utilis� pour d�clarer des classes abstraites

# Classe abstraite qui d�finit le contrat
class Case(object):

     # Marqueurs de propri�t� abstraite
    @property
    @abstractmethod 
    def texture(self): # Texture de la case
        pass

    @abstractmethod # Marqueur de m�thode abstraite
    def handleClick(event): # Traiter l'�v�nement de clic
        pass

class Sure(Case):
    """ Case non creus�e ne cachant pas de bombe """
    def handleClick(event):
        pass

class Vide(Case):
    """ Case creus�e """

    def __init__(self, nbBombesVoisines: int):
        if nbBombesVoisines > 0 and nbBombesVoisines < 8:
            self.nbBombesVoisines = nbBombesVoisines
        else:
            raise ValueError("Le nombre de bombes voisines doit �tre entre 0 (aucune) et 8 (toutes les cases voisines).")

    def handleClick(event):
        pass

class Drapeau(Case):
    """ Case contenant un drapeau pla�� par le joueur, marquant ou non l'emplacememnt d'une bombe. """

    def __init__(self, surBombe: bool):
        self.surBombe = surBombe

class Bombe(Case):
    """ Case cachant une bombe"""
    def handleClick(event):
        pass

class Explosee(Case):
    """ Case contenant une bombe explos�e """
    def handleClick(event):
        pass