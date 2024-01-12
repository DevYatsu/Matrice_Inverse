from determinant import determinant
from utils import print_matrice


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

    n = len(matrice)
    matrice_inverse = [
        [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for numero_ligne_pivot in range(n):
        # element de la diagonale de la matrice dans la ligne correspondante
        pivot = matrice[numero_ligne_pivot][numero_ligne_pivot]

        # on fait en sorte que le pivot devienne 1 en divisant chaque element de la ligne pivot par le "pivot"/nombre dans la diagonale
        for j in range(n):
            matrice[numero_ligne_pivot][j] /= pivot

            # on divise aussi dans la matrice inverse
            matrice_inverse[numero_ligne_pivot][j] /= pivot

        for i in range(n):
            if i == numero_ligne_pivot:
                # on saute la ligne pivot
                continue

            # on recupere le nombre sur la meme colonne que le nombre pivot du debut
            coefficient = matrice[i][numero_ligne_pivot]

            # Soustraction de la ligne pivot multipliée par le coefficient pour obtenir des 0 partout sauf diagonales
            for j in range(n):
                matrice[i][j] -= coefficient * matrice[numero_ligne_pivot][j]
                matrice_inverse[i][j] -= coefficient * \
                    matrice_inverse[numero_ligne_pivot][j]

    print("Matrice inverse:")
    print_matrice(matrice_inverse)

    return matrice_inverse


matrice_0 = [
    [4, 5],
    [1, 1]
]

m = [[1, 2], [3, 4]]

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

test = [
    [1,1,2],
    [1,2,1],
    [2,1,1]
]

# inverse(matrice_0)
inverse(test)
