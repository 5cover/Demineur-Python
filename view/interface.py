import tkinter as tk
import controller.config as config
from controller.config import largeurGrille, hauteurGrille
import controller.clics as clics

_labels = []
_fenetrePrincipale = tk.Tk()
_imagesChargees = {}

def creerFenetrePrincipale():
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
    texte = ""
    if case == config.case.VIDE and nbBombesVoisines > 0:
        texte = str(nbBombesVoisines)
    return texte

def creerLabelCase():
    label = tk.Label(master=_fenetrePrincipale, compound='center', bd=0, font=("Segoe 10 bold"), padx=0, pady=0)
    label.bind('<Button>', caseClic)
    _labels.append(label)
    return label

def recupererImageCase(case: config.case, label):
    img = tk.PhotoImage(master=_fenetrePrincipale, file=config.CHEMIN_DOSSIER_TEXTURES + case.value)
    _imagesChargees[label] = img
    return img

def caseClic(event):
    clics.caseClic(event.widget.grid_info()["column"], event.widget.grid_info()["row"], event.num)
    actualiserLabels()

def partiePerdue():
    _fenetrePrincipale.title("Partie perdue !")
    _fenetrePrincipale.bell()

def partieGagnee():
    _fenetrePrincipale.title("Partie gagnée !")
    _fenetrePrincipale.bell()

def nouvellePartie():
    _fenetrePrincipale.title("Démineur 2020")
    config.genererGrille(largeurGrille(), hauteurGrille(), config.nbBombes)