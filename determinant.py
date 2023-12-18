def trouver_sous_matrice(index: int, matrice: list[list[int]]):
    sous_matrice = [row[:] for row in matrice[1:]]

    for line in sous_matrice:
        line.pop(index)

    return sous_matrice


def determinant(matrice: list[list[int]]):
    # calculer le determinant revient à faire des soustractions et additions de la multiplication d'un coefficient avec une sous-matrice de notre matrice
    # On sait calculer le determinant d'une matrice 2*2
    # Pour obtenir le determinant d'un matrice de taille supérieure, il faut donc se retrouver à un moment ou un autre avec une matrice 2*2
    # EXEMPLE CI-DESSOUS
    # Matrice 3x3
    # [
    #  [a1,a2,a3],
    #  [a4,a5,a6]
    #  [a7,a8,a9]
    # ]
    # On peut prendre les coefficients sur une ligne ou une colonne,
    # Le plus simple est de prendre les coefficients de la 1ere ligne de la matrice
    # Ainsi on se retrouve avec [a1, a2, a3] comme coefficients
    #
    # On multiplie a1 avec le déterminant de la matrice formée en supprimant les colonnes et lignes contenant a1
    # det([
    #  [a5, a6],
    #  [a8, a9]
    # ])
    # Puis on fait de même avec a2
    # Ici on prend les 2 colonnes qui ne se trouvent pas dans la ligne ou la colonne de a2
    # C'est à dire [a4] et [a6] soit la matrice [a4, a6]
    #              [a7]    [a9]                 [a7, a9]
    # Ainsi on a:
    # det([
    #  [a4, a6],
    #  [a7, a9]
    # ])
    # Puis on fait de même avec a3
    # det([
    #  [a4, a5],
    #  [a7, a8]
    # ])
    #
    # Pour calculer le determinant de notre MATRICE 3*3:
    # a1 * det([[a5, a6], [a8, a9]]) - a2 * det([[a4, a6],[a7, a9]]) + a3 * det([[a4, a5],[a7, a8]])
    # Il faut alterner entre addition et soustraction

    matrice = matrice[:]
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
