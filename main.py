import view.interface as interface
import controller.config as config

grilleEtBombes = config.genererGrilleEtBombes(6, 12, 1)

interface.init(grilleEtBombes[0], grilleEtBombes[1])

interface.creerFenetrePrincipale().mainloop()