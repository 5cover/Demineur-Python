import tkinter as tk
import controller.config as config
from controller.config import largeurGrille, hauteurGrille
import controller.clics as clics

_labels = []
_fenetrePrincipale = tk.Tk()
# Les textures des cases sont stockées ici afin d'éviter qu'elles soient supprimées par le ramasse-miettes.
_imagesChargees = {}

def creerFenetrePrincipale():
    """ Création, construction et retour de la fenêtre du jeu.  """
    # la taille de la fenêtre est adaptéee à la taille de la grille de jeu
    _fenetrePrincipale.geometry(f"{largeurGrille()*config.COTE_CASE}x{hauteurGrille()*config.COTE_CASE}")
    _fenetrePrincipale.resizable(False, False) # désactiver le redimensionnement
    _fenetrePrincipale.title("Démineur 2020") # titre
    _fenetrePrincipale.iconbitmap('.\\model\\icon.ico') # icône
    
    for iColonne in range(largeurGrille()):
        _fenetrePrincipale.columnconfigure(iColonne)
    for iLigne in range(hauteurGrille()):
        _fenetrePrincipale.rowconfigure(iLigne)

    for colonne in range(largeurGrille()):
        for ligne in range (hauteurGrille()):
            creerLabelCase().grid(column = colonne, row = ligne)

    actualiserLabels()

    return _fenetrePrincipale

def actualiserLabels():
    """ Actualisation des labels correspondant à chaque case. Rénitialisation de leur image d'arrière plan, texte et couleur du texte. """
    for label in _labels:
        colonne = label.grid_info()["column"]
        ligne = label.grid_info()["row"]
        case = config.grille[colonne][ligne]
        nbBombesVoisines = config.compterBombesVoisines(colonne, ligne)

        label["image"] = recupererImageCase(case, label)
        label["text"] = obtenirTexteCase(nbBombesVoisines, case)
        if nbBombesVoisines > 0:
            label["fg"] = config.choisirCouleur(nbBombesVoisines)

def obtenirTexteCase(nbBombesVoisines, case: config.case):
    """ Obtention du texte à afficher sur une case. """
    texte = ""
    if case == config.case.VIDE and nbBombesVoisines > 0:
        texte = str(nbBombesVoisines)
    return texte

def creerLabelCase():
    """ Création d'un label utilisé pour représenter une case sur la grille. """
    label = tk.Label(master=_fenetrePrincipale, compound='center', bd=0, font=("Segoe 10 bold"), padx=0, pady=0)
    # Ici, la fonction bind() permet de s'abonner à l'évènement de clic du label.
    label.bind('<Button>', caseClic)
    _labels.append(label)
    return label

def recupererImageCase(case: config.case, label):
    """ Récupération et traitement de l'image correspondant à la valeur de la case spécifiée. """
    img = tk.PhotoImage(master=_fenetrePrincipale, file=config.CHEMIN_DOSSIER_TEXTURES + case.value)
    _imagesChargees[label] = img
    return img

def caseClic(event):
    """ Récupération et transfert de l'évènement de clic, avec des informations supplémentaires vers le module clics.
    Ces informations sont :
    - L'emplacement de la case cliquée (avec la fonction event.widget.grid_info()) ;
    - Le numéro du bouton de la souris cliquée (avec event.num). 3 valeurs sont prises en charge :
        - 1 pour le bouton gauche ;
        - 2 pour le bouton de la molette ;
        - 3 pour le bouton droit. """
    clics.caseClic(event.widget.grid_info()["column"], event.widget.grid_info()["row"], event.num)
    actualiserLabels()

def partiePerdue():
    """ Modifie du titre de la fenêtre et jouer un son pour signaler à l'utilisateur que la partie est perdue. """
    _fenetrePrincipale.title("Partie perdue !")
    _fenetrePrincipale.bell()

def partieGagnee():
    """ Modifie du titre de la fenêtre et jouer un son pour signaler à l'utilisateur que la partie est gagnée. """
    _fenetrePrincipale.title("Partie gagnée !")
    _fenetrePrincipale.bell()

def nouvellePartie():
    """ Recréation de la grille pour commencer une nouvelle partie. """
    _fenetrePrincipale.title("Démineur 2020")
    config.genererGrille(largeurGrille(), hauteurGrille(), config.nbBombes)