from determinant import soustraction_matrices, addition_matrices, multiplication_nombre_avec_matrice
from utils import gen_matrice_inverse


def verif_si_matrice_valide(matrice: list[list[int]]):
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


def inverse(matrice: list[list[int]]):
    verif_si_matrice_valide(matrice)
    matrice_inv_initiale = gen_matrice_inverse(matrice.copy())

    return ""


matrice_0 = [
    [0, 0],
    [1, 1]
]
matrice_1 = [
    [0, 0, 5, 6],
    [1, 1, 2, 4],
    [9, 3, 2, 4],
    [8, 0, 2, 4]
]

inverse(matrice_0)
inverse(matrice_1)

print(multiplication_nombre_avec_matrice(2, matrice_1))
