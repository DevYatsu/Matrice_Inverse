from utils import gen_matrice_nulle


def addition_matrices(matrice_1: list[list[int]], matrice_2: list[list[int]]):
    matrice = gen_matrice_nulle(matrice_1)

    for index_de_la_ligne, ligne in enumerate(matrice):
        matrice[index_de_la_ligne] = [
            matrice_1[index_de_la_ligne][index_dans_ligne] +
            matrice_2[index_de_la_ligne][index_dans_ligne]
            for index_dans_ligne, _ in enumerate(ligne)
        ]

    return matrice


def soustraction_matrices(matrice_1: list[list[int]], matrice_2: list[list[int]]):
    matrice = gen_matrice_nulle(matrice_1)

    for index_de_la_ligne, ligne in enumerate(matrice):
        matrice[index_de_la_ligne] = [
            matrice_1[index_de_la_ligne][index_dans_ligne] -
            matrice_2[index_de_la_ligne][index_dans_ligne]
            for index_dans_ligne, _ in enumerate(ligne)
        ]

    return matrice


def multiplication_nombre_avec_matrice(nombre: int, matrice: list[list[int]]):
    matrice = matrice.copy()

    for index_de_la_ligne, ligne in enumerate(matrice):
        matrice[index_de_la_ligne] = [
            matrice[index_de_la_ligne][index_dans_ligne] * nombre
            for index_dans_ligne, _ in enumerate(ligne)
        ]

    return matrice


def determinant(matrice: list[list[int]]):
    matrice = matrice.copy()
    main_line = matrice[0]
