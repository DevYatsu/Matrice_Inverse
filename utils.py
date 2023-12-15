def gen_matrice_nulle(matrice: list[list[int]]):
    # fonction utilisée pour éviter de modifier les valeurs de la matrice initiale directement

    return list(map(lambda x: [0] * len(x), matrice))


def gen_matrice_inverse(matrice_base: list[list[int]]):
    matrice = gen_matrice_nulle(matrice_base)
    for i, _ in enumerate(matrice):
        matrice[i][i] = 1
    return matrice


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
    matrice = matrice[0:]

    for index_de_la_ligne, ligne in enumerate(matrice):
        matrice[index_de_la_ligne] = [
            matrice[index_de_la_ligne][index_dans_ligne] * nombre
            for index_dans_ligne, _ in enumerate(ligne)
        ]

    return matrice
