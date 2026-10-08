#!/usr/bin/python3
"""Module de validation d'un encodage UTF-8.

Fournit une fonction qui vérifie si une liste d'entiers (chacun
représentant un octet) forme une séquence UTF-8 valide.
"""


def count_ones_left(data):
    """Compte les bits à 1 consécutifs en partant du bit de poids fort.

    En UTF-8, ce nombre indique le rôle de l'octet :
        0     -> caractère ASCII sur 1 octet (0xxxxxxx)
        1     -> octet de continuation (10xxxxxx)
        2 à 4 -> premier octet d'un caractère sur 2 à 4 octets

    Args:
        data (int): l'octet à analyser (seuls les 8 bits de poids
            faible sont pris en compte).

    Returns:
        int: le nombre de '1' consécutifs en tête de l'octet.
    """
    count = 0

    # On parcourt les bits du 7e (poids fort) au 0e (poids faible)
    for i in range(7, -1, -1):
        if data & (1 << i):
            count += 1
        else:
            # Premier '0' rencontré : la suite de '1' est terminée
            break
    return count


def validUTF8(data):
    """Détermine si un ensemble de données est un encodage UTF-8 valide.

    Args:
        data (list[int]): liste d'entiers, chacun représentant un octet.

    Returns:
        bool: True si data est un encodage UTF-8 valide, sinon False.
    """
    # Nombre d'octets de continuation encore attendus pour le
    # caractère en cours de lecture
    remaining = 0

    for d in data:
        if not remaining:
            # On attend le début d'un nouveau caractère
            remaining = count_ones_left(d)
            if remaining == 0:
                # Caractère ASCII sur un seul octet
                continue
            elif remaining == 1 or remaining > 4:
                # Une continuation ne peut pas commencer un caractère,
                # et UTF-8 limite un caractère à 4 octets
                return False
        else:
            # On est au milieu d'un caractère : l'octet doit être
            # une continuation de la forme 10xxxxxx
            if count_ones_left(d) != 1:
                return False
        # Un octet du caractère courant vient d'être consommé
        remaining -= 1

    # Valide seulement si le dernier caractère est complet
    return remaining == 0
