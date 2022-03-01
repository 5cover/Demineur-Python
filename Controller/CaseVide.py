import Case

class CaseVide(Case):
    """ Creusée """

    def __init__(self, nbBombesVoisines):
        if nbBombesVoisines > 0 and nbBombesVoisines < 8:
            self.nbBombesVoisines = nbBombesVoisines
        else:
            raise ValueError("Le nombre de bombes voisines doit être entre 0 (aucune) et 8 (toutes les cases voisines).")


