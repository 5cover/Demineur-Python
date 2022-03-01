from abc import ABC, abstractmethod # Module utilisé pour déclarer des classes abstraites


class Case(object):

     # Marqueurs de propriété abstraite
    @property
    @abstractmethod 
    def texture(self): # Texture de la case
        pass

    @abstractmethod # Marqueur de méthode abstraite
    def handleClick(event): # Traiter l'évènement de clic
        pass




