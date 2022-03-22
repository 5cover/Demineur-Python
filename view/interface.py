import tkinter as tk
import controller.config as config

_grille = None
_bombes = None
_labels = []
_fenetrePrincipale = tk.Tk()
_imagesChargees = {}

def init(grille, bombes):
    global _grille
    global _bombes
    _grille = grille
    _bombes = bombes

def creerFenetrePrincipale():

    _fenetrePrincipale.geometry("640x640") # taille
    _fenetrePrincipale.resizable(False, False) # désactiver le redimensionnement
    _fenetrePrincipale.title("Démineur 2020") # titre
    _fenetrePrincipale.iconbitmap('.\\model\\icon.ico') # icône
    
    for iColonne in range(len(_grille)):
        _fenetrePrincipale.columnconfigure(iColonne)
    for iLigne in range(len(_grille[0])):
        _fenetrePrincipale.rowconfigure(iLigne)

    for ligne in range(len(_grille)):
        for colonne in range (len(_grille[0])):
            creerLabelCase().grid(column = colonne, row = ligne)
    
    actualiserLabels()
    return _fenetrePrincipale


def actualiserLabels():
    for label in _labels:
        ligne = label.grid_info()["row"]
        colonne = label.grid_info()["column"]

        case = _grille[ligne][colonne]
        nbBombesVoisines = config.compterBombesVoisines(ligne, colonne, _bombes)

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
    ligne = event.widget.grid_info()["row"]
    colonne = event.widget.grid_info()["column"]
    if event.num == 1:
        caseClicGauche(ligne, colonne)
    elif event.num == 3:
        caseClicDroit(ligne, colonne)
    actualiserLabels()

def caseClicGauche(ligne, colonne):
    if _bombes[ligne][colonne] and _grille[ligne][colonne] != config.case.DRAPEAU:
        perdre()
    elif _grille[ligne][colonne] == config.case.PLEINE:
        _grille[ligne][colonne] = config.case.VIDE
    
def perdre():
    for ligne in range(len(_grille)):
        for colonne in range (len(_grille[0])):
            if _bombes[ligne][colonne]:
                _grille[ligne][colonne] = config.case.EXPLOSEE

def caseClicDroit(ligne, colonne):
    if _grille[ligne][colonne] == config.case.PLEINE:
        _grille[ligne][colonne] = config.case.DRAPEAU
    elif _grille[ligne][colonne] == config.case.DRAPEAU:
        _grille[ligne][colonne] = config.case.PLEINE
