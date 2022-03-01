from abc import ABC, abstractmethod # Module utilis� pour d�clarer des classes abstraites


class Case(object):

     # Marqueurs de propri�t� abstraite
    @property
    @abstractmethod 
    def texture(self): # Texture de la case
        pass

    @abstractmethod # Marqueur de m�thode abstraite
    def handleClick(event): # Traiter l'�v�nement de clic
        pass




