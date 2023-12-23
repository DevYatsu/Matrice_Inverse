def gen_matrice_nulle(matrice: list[list[float]]):
    n = len(matrice)
    matrice_nulle = [[0] * n for _ in range(n)]

    return matrice_nulle


def addition_matrices(matrice_1: list[list[float]], matrice_2: list[list[float]]):
    matrice = gen_matrice_nulle(matrice_1)

    for index_de_la_ligne, ligne in enumerate(matrice):
        matrice[index_de_la_ligne] = [
            matrice_1[index_de_la_ligne][index_dans_ligne] +
            matrice_2[index_de_la_ligne][index_dans_ligne]
            for index_dans_ligne, _ in enumerate(ligne)
        ]

    return matrice


def soustraction_matrices(matrice_1: list[list[float]], matrice_2: list[list[float]]):
    matrice = gen_matrice_nulle(matrice_1)

    for index_de_la_ligne, ligne in enumerate(matrice):
        matrice[index_de_la_ligne] = [
            matrice_1[index_de_la_ligne][index_dans_ligne] -
            matrice_2[index_de_la_ligne][index_dans_ligne]
            for index_dans_ligne, _ in enumerate(ligne)
        ]

    return matrice


def multiplication_nombre_avec_matrice(nombre: float, matrice: list[list[float]]):
    matrice = matrice[0:]

    for index_de_la_ligne, ligne in enumerate(matrice):
        matrice[index_de_la_ligne] = [
            matrice[index_de_la_ligne][index_dans_ligne] * nombre
            for index_dans_ligne, _ in enumerate(ligne)
        ]

    return matrice


def print_matrice(matrice: list[list[float]]):
    string = "[\n"
    for line in matrice:
        string += "  "
        string += "\t".join([str(element) for element in line]) + "\n"

    string += "]"
    print(string)
