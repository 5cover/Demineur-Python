import Case

class CaseVide(Case):
    """ Creus�e """

    def __init__(self, nbBombesVoisines):
        if nbBombesVoisines > 0 and nbBombesVoisines < 8:
            self.nbBombesVoisines = nbBombesVoisines
        else:
            raise ValueError("Le nombre de bombes voisines doit �tre entre 0 (aucune) et 8 (toutes les cases voisines).")


