import tkinter as tk

window = tk.Tk()

window.geometry("300x250") # taille de la fenêtre
window.resizable(False, False) # désactiver le redimensionnement
window.title("Démineur") # titre de la fenêtre

hey = tk.Label(text="Démineur")
hey.pack()

window.mainloop()
