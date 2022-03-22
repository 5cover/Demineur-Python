import view.interface as interface
import controller.config as config

grilleEtBombes = config.genererGrilleEtBombes(10, 10, 10)

interface.init(grilleEtBombes[0], grilleEtBombes[1])

interface.creerFenetrePrincipale().mainloop()