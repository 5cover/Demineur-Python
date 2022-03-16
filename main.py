import view.interface as interface
import controller.config as config

grilleEtBombes = config.genererGrilleEtBombes(12, 12, 3)

interface.creerFenetrePrincipale(grilleEtBombes[0], grilleEtBombes[1]).mainloop()