import controller.config as config

def caseClicGauche(case: config.case, bombe: bool):
    """ Réponse à un clic gauche sur une case """
    # La case cliquée contient une bombe et l'utilisateur n'a pas placé de drapeau dessus
    if bombe and case != config.case.DRAPEAU:
        # La partie est perdue
        print(4)
    # La case cliquée est une case pleine qui ne contient pas de bombe.
    elif case == config.case.PLEINE:
        # la case est creusée
        case = config.case.VIDE

    print(case)

def caseClicDroit(case: config.case):
    """ Réponde à une clic droit sur une case """

    # L'utilisateur souhaite placer un drapeau sur la case
    if case == config.case.PLEINE:
        # Un drapeau est placé
        case = config.case.DRAPEAU

    # L'utilisateur souhaite enlever le drapeau de la case
    elif case == config.case.DRAPEAU:
        # Le drapeau est enlevé
        case = config.case.PLEINE
