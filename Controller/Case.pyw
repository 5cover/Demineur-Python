from abc import ABC, abstractmethod # Module utilisé pour déclarer des classes abstraites

# Classe abstraite qui définit le contrat
class Case(object):

     # Marqueurs de propriété abstraite
    @property
    @abstractmethod 
    def texture(self): # Texture de la case
        pass

    @abstractmethod # Marqueur de méthode abstraite
    def handleClick(event): # Traiter l'évènement de clic
        pass

class Sure(Case):
    """ Case non creusée ne cachant pas de bombe """
    def handleClick(event):
        pass

class Vide(Case):
    """ Case creusée """

    def __init__(self, nbBombesVoisines: int):
        if nbBombesVoisines > 0 and nbBombesVoisines < 8:
            self.nbBombesVoisines = nbBombesVoisines
        else:
            raise ValueError("Le nombre de bombes voisines doit être entre 0 (aucune) et 8 (toutes les cases voisines).")

    def handleClick(event):
        pass

class Drapeau(Case):
    """ Case contenant un drapeau plaçé par le joueur, marquant ou non l'emplacememnt d'une bombe. """

    def __init__(self, surBombe: bool):
        self.surBombe = surBombe

class Bombe(Case):
    """ Case cachant une bombe"""
    def handleClick(event):
        pass

class Explosee(Case):
    """ Case contenant une bombe explosée """
    def handleClick(event):
        pass