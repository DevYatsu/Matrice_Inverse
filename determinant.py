def trouver_sous_matrice(index: int, matrice: list[list[int]]):
    # trouver la matrice qu'il faut multiplier par le nombre de la ligne d'en haut avec son index
    # EXEMPLE CI-DESSOUS
    # Matrice 3x3
    # [
    #  [a1,a2,a3],
    #  [a4,a5,a6]
    #  [a7,a8,a9]
    # ]
    # On veut trouver le determinant de la sous-matrice à multiplier avec le nombre a1
    # cette sous matrice est
    # det([
    #  [a5, a6],
    #  [a8, a9]
    # ])
    # Puis a2
    # cette sous matrice est
    # det([
    #  [a4, a6],
    #  [a7, a9]
    # ])
    # On soustrait les resultats obtenus puis on additionne le resultat de a3 par [[a4,a5], [a7, a8]]

    sous_matrice = [row[:] for row in matrice[1:]]

    for line in sous_matrice:
        line.pop(index)

    return sous_matrice


def determinant(matrice: list[list[int]]):
    matrice = matrice[0:]
    if len(matrice) == 2:
        return matrice[0][0] * matrice[1][1] - matrice[1][0] * matrice[0][1]

    main_line = matrice[0]

    sum = 0

    for index, a in enumerate(main_line):
        if a == 0:
            # on saute les 0 car 0*x = 0
            continue

        sous_matrice = trouver_sous_matrice(
            index, matrice)

        sous_det = determinant(sous_matrice)
        sum += ((-1) ** index) * a * sous_det

    return sum
