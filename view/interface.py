import tkinter as tk
from tkinter import ttk # Widgets à thèmes
import controller.config as config

def creerFenetrePrincipale(grille, bombes):

    fenetre = tk.Tk()

    fenetre.geometry("640x640") # taille
    fenetre.resizable(False, False) # désactiver le redimensionnement
    fenetre.title("Démineur 2020") # titre
    fenetre.iconbitmap('.\\model\\icon.ico') # icône

    for iColonne in range(len(grille)-1):
        fenetre.columnconfigure(iColonne)
    for iLigne in range(len(grille[0])-1):
        fenetre.rowconfigure(iLigne)

    for i in range(len(grille)-1):
        for j in range (len(grille[0])-1):
            texte = ""
            if grille[i][j] == config.case.VIDE:
                nbBombesVoisines = config.compterBombesVoisines(i, j, bombes)
                if nbBombesVoisines > 0:
                    texte = str(nbBombesVoisines)
            creerLabelCase(fenetre, grille[i][j], texte).grid(column = i, row = j, sticky="NESW")
            

    return fenetre


def creerLabelCase(fenetre, case: config.case, texte):
    img = tk.PhotoImage(file = config.CHEMIN_DOSSIER_TEXTURES + case.value, width=config.COTE_CASE, height=config.COTE_CASE)
    imagesCharges.append(img)
    return tk.Label(fenetre, text=texte, image=img, compound='center', width=config.COTE_CASE, height=config.COTE_CASE, bd=0)

# Ce tableau sert à stocker les images produites par creerWidget, afin qu'elles ne soient pas "garbage-collected" (supprimées automatiqument par Python pour libérer de la mémoire)
imagesCharges = []

