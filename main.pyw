import view.interface as interface
import controller.config as config

if __name__ == "__main__":
    config.genererGrille(10, 10, 15)
    interface.creerFenetrePrincipale().mainloop()