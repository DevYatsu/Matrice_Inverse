from determinant import determinant
from utils import gen_matrice_inverse, print_matrice


def verif_si_matrice_valide(matrice: list[list[float]]):
    longueur_matrice = len(matrice)

    for ligne in matrice:
        longueur_ligne = len(ligne)
        if longueur_ligne != longueur_matrice:
            # erreur si matrice non carré
            raise Exception(
                f"Petit Malin! Ta matrice doit être carré! \n Or {matrice} ne l'est pas!")

        if not all(isinstance(item, int) for item in ligne):
            # erreur si matrice ne contient pas que des nombres
            raise Exception(
                f"Petit Malin! Ta matrice ne doit contenir que des nombres! \n Or ce n'est pas le cas pour {matrice}!")


def inverse(matrice: list[list[float]]):
    verif_si_matrice_valide(matrice)

    det = determinant(matrice)
    print(f"determinant: {det}")

    if det == 0.0:
        # mauvaise pratique pour créer des erreurs mais ce n'est pas important ici
        raise Exception(
            f"det = 0! Pas d'inverse existant pour la matrice: {matrice}")

    MATRICE_INVERSE = gen_matrice_inverse(len(matrice))
    matrice_inverse = [row[:] for row in MATRICE_INVERSE[:]]

    # maintenant definir la ligne pivot puis annuler les valeurs pour trouver des 0 sauf dans les diagonales
    # while MATRICE_INVERSE != matrice:
    #     matrice

    for colonne in range(len(matrice)):
        for ligne in range(len(matrice)):
            if colonne == ligne:
                continue

            pivot = matrice[colonne]
            coefficient = matrice[ligne][colonne]

            matrice[ligne] = [num * pivot[colonne] - coefficient *
                              pivot[i] for i, num in enumerate(matrice[ligne])]

            # on fait pareil avec la matrice inverse
            matrice_inverse[ligne] = [num * pivot[colonne] - coefficient *
                                      pivot[i] for i, num in enumerate(matrice_inverse[ligne])]

    for ligne in range(len(matrice)):
        coeff = matrice[ligne][ligne]
        if coeff != 0:
            matrice[ligne][ligne] /= coeff  # == 1

        for colonne in range(len(matrice_inverse[ligne])):
            if coeff != 0:
                matrice_inverse[ligne][colonne] /= coeff

    print(matrice)
    print_matrice(matrice_inverse)

    return ""


matrice_0 = [
    [4, 5],
    [1, 1]
]

m = [[4, 5], [1, 1]]

matrice_1 = [
    [1, 0, 5, 6],
    [1, 1, 2, 4],
    [9, 3, 7, 6],
    [8, 0, 2, 4]
]

matrice_2 = [
    [10475, 000, 5200, 60090],
    [1760, 100, 2040, 40290],
    [9102, 300, 7300, 63090],
    [8010, 00, 2001, 41090]
]

# inverse(matrice_0)
inverse(matrice_1)
