def gen_matrice_nulle(matrice: list[list[int]]):
    # fonction utilisée pour éviter de modifier les valeurs de la matrice initiale directement

    return list(map(lambda x: [0] * len(x), matrice))


def gen_matrice_inverse(matrice_base: list[list[int]]):
    matrice = gen_matrice_nulle(matrice_base)
    for i, _ in enumerate(matrice):
        matrice[i][i] = 1
    return matrice
