#!/usr/bin/python3
"""Module qui détermine le gagnant du jeu des nombres premiers."""


def isWinner(x, nums):
    """Retourne le nom du joueur qui a gagné le plus de manches, ou None."""
    # x = nombre de manches jouées (ex : 5).
    # nums = liste des n de chaque manche (ex : [2, 5, 1, 4, 3]).
    if not nums or x < 1:
        return None

    # max_n = le plus grand n de la liste (ex : 5).
    # Inutile de chercher des nombres premiers au-delà.
    max_n = max(nums)

    # Si max_n vaut 0 ou 1, il n'y a aucun premier : Maria ne peut
    # jamais jouer, donc Ben gagne toutes les manches.
    if max_n < 2:
        return "Ben"

    # crible = liste de True/False, comme une passoire qui ne garde
    # que les nombres premiers.
    # crible[3] = True -> 3 est premier.
    # crible[4] = False -> 4 n'est pas premier.
    crible = [True] * (max_n + 1)

    # 0 et 1 ne sont pas des nombres premiers.
    crible[0] = crible[1] = False

    # i = le nombre qu'on examine (2, 3, 4...).
    # On s'arrête à la racine carrée de max_n, c'est suffisant.
    for i in range(2, int(max_n ** 0.5) + 1):
        # Si i est encore premier, on barre tous ses multiples.
        if crible[i]:
            # j = les multiples de i (si i = 2 : 4, 6, 8...).
            for j in range(i * i, max_n + 1, i):
                crible[j] = False

    # nb_premiers[i] = combien de nombres premiers entre 1 et i.
    # Ex : nb_premiers[5] = 3, car il y a 2, 3 et 5.
    nb_premiers = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        # On reprend le total précédent et on ajoute 1 si i est premier.
        nb_premiers[i] = nb_premiers[i - 1] + (1 if crible[i] else 0)

    # maria et ben = compteurs de manches gagnées, ils démarrent à 0.
    maria = 0
    ben = 0

    # n = le nombre d'une seule manche.
    # nums[:x] = on ne garde que les x premières manches.
    for n in nums[:x]:
        # Chaque tour retire un premier, donc nombre de tours =
        # nombre de premiers. Maria joue les tours 1, 3, 5...
        # Impair -> Maria joue le dernier coup et gagne.
        # Pair -> Ben joue le dernier coup et gagne.
        if nb_premiers[n] % 2 == 1:
            maria += 1
        else:
            ben += 1

    # Celui qui a le plus de victoires gagne la partie.
    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"

    # Égalité : on ne peut pas désigner de gagnant.
    return None
