import tkinter as tk
import controller.config as config
from controller.config import largeurGrille, hauteurGrille
from controller.clics import caseClicGauche, caseClicDroit
from itertools import chain

_labels = []
_fenetrePrincipale = tk.Tk()
_imagesChargees = {}

def creerFenetrePrincipale():
    _fenetrePrincipale.geometry("640x480") # taille
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

    _fenetrePrincipale.mainloop()

    return _fenetrePrincipale


def actualiserLabels():
    for label in _labels:
        colonne = label.grid_info()["column"]
        ligne = label.grid_info()["row"]
        case = config.grille[colonne][ligne]
        nbBombesVoisines = config.compterBombesVoisines(colonne, ligne)

        label["image"] = recupererImageCase(case, label)
        label["text"] = obtenirTexteCase(nbBombesVoisines, case)
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

    colonne = event.widget.grid_info()["column"]
    ligne = event.widget.grid_info()["row"]

    case = config.grille[colonne][ligne]
    bombe = config.bombes[colonne][ligne]

    if event.num == 1:
        caseClicGauche(case, bombe)
    elif event.num == 3:
        caseClicDroit(case)

    actualiserLabels()

def creuserPourLaPremiereFois(l, c):
    creuser(l, c)
    
    for i in range(0, largeurGrille()):
        for j in chain(reversed(range(0, c)), range(c, hauteurGrille())):
            if config.compterBombesVoisines(i, j) > 0:
                break
            creuser(i, j)

def creuser(c, l):
    config.grille[c][l] = config.case.VIDE

def perdre():
    """ Perdre la partie et révéler toutes les bombes. """
    for ligne in range(largeurGrille()):
        for colonne in range (hauteurGrille()):
            if config.bombes[ligne][colonne]:
                config.grille[ligne][colonne] = config.case.EXPLOSEE