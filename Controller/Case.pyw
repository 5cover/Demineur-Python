from abc import abstractmethod # Module utilisé pour déclarer des classes abstraites

class Case(object):

     # Marqueurs de propriété abstraite
    @property
    @abstractmethod 
    def texture(self):
    """ Chaîne de caractère correspondant au chemin de l'image de la texture de la case. """
        pass

    @abstractmethod # Marqueur de méthode abstraite
    def handleClick(event):
    """ Méthode destinée à traiter l'évènement de clic sur la case. """
        pass

class Sure(Case):
    """ Case non creusée ne cachant pas de bombe """

    @property
    def texture(self):
        pass

    def handleClick(event):
        pass

class Vide(Case):
    """ Case creusée """
    
    @property
    def nbBombesVoisines(self):
        return self.nbBombesVoisines

    @nbBombesVoisines.setter
    def nbBombesVoisines(self, value):
        if nbBombesVoisines > 0 and nbBombesVoisines < 8:
            self.nbBombesVoisines = nbBombesVoisines
        else:
            raise ValueError("Le nombre de bombes voisines doit être entre 0 (aucune) et 8 (toutes les cases voisines).")

    @property
    def texture(self):
        pass

    def __init__(self, nbBombesVoisines: int):
        self.nbBombesVoisines = nbBombesVoisines

    def handleClick(event):
        pass

class Drapeau(Case):
    """ Case contenant un drapeau plaçé par le joueur, marquant ou non l'emplacememnt d'une bombe.
    Un chiffre de 0 à 8 s'affiche dessus selon le nombre de cases voisines contenant une bombe."""

    @property
    def texture(self):
        pass

    def __init__(self, surBombe: bool):
        self.surBombe = surBombe

class Bombe(Case):
    """ Case cachant une bombe"""

    @property
    def texture(self):
        pass

    def handleClick(event):
        pass

class Explosee(Case):
    """ Case contenant une bombe explosée """

    @property
    def texture(self):
        pass

    def handleClick(event):
        pass