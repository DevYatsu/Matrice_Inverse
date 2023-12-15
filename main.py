from determinant import determinant
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
    
    det = determinant(matrice)
    if det == 0:
        raise Exception(
            f"Determinant = 0! Pas d'inverse existant pour la matrice: {matrice}")
        
    matrice_inv_initiale = gen_matrice_inverse(matrice)
    
    # maintenant definir la ligne pivot puis annuler les valeurs pour trouver des 0 sauf dans les diagonales

    return ""


matrice_0 = [
    [4, 5],
    [1, 1]
]
matrice_1 = [
    [0, 0, 5, 6],
    [1, 1, 2, 4],
    [9, 3, 7, 6],
    [8, 0, 2, 4]
]

# inverse(matrice_0)
# inverse(matrice_1)

print(determinant(
    matrice_0))
