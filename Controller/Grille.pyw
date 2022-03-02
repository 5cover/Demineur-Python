from random import randint

import Case

class Grille(object):

    @property
    def matrice(self)
        return self._matrice

    def __init__(self, hauteur: int, largeur: int, nombreBombes: int):
        
        if hauteur < 0 or largeur < 0:
            raise new ValueError("La hauteur et la largeur doivent �tre positives.")
        if nombreBombes < 0 or nombreBombes > hauteur * largeur:
            raise new ValueError("Le nombre de bombes doit se trouver entre 0 et le nombre total de cases.")
        
        self._matrice = [[new Case.Vide()] * hauteur for _ in range largeur]

        while nombreBombes > 0:

            # Choisir un emplacement al�atoire sur la grille
            ligne = randint(0, hauteur-1)
            colonne = randint(0, largeur-1)

            # Si il n'y a pas d�j� une bombe, placer une bombe et d�cr�menter le variant de boucle nombreBombes
            # qui repr�sente le nombre de bombes restantes � placer.
            if isinstance(_matrice[ligne][colonne], Case.Bombe()):
                _matrice[ligne][colonne] = new Case.Bombe()
                nombreBombes -= 1
            





