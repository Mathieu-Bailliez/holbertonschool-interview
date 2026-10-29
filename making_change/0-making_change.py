#!/usr/bin/python3
"""Module that determines the fewest coins needed to meet a total."""


def makeChange(coins, total):
    """Return the fewest coins needed to meet total, or -1 if impossible."""
    # ---------------------------------------------------------------
    # L'IDÉE GÉNÉRALE
    # Au lieu de chercher directement la réponse pour "total",
    # on calcule la réponse pour chaque montant plus petit :
    # 0, puis 1, puis 2... jusqu'à "total".
    # Chaque nouvelle réponse se sert des réponses déjà trouvées.
    #
    # Exemple avec les pièces [1, 2] et total = 4 :
    #   si on paie 4 avec une pièce de 2, il reste 2 à payer ;
    #   on sait déjà que 2 se paie avec 1 pièce ;
    #   donc 4 se paie avec 1 + 1 = 2 pièces.
    # ---------------------------------------------------------------

    # ÉTAPE 1 : le cas le plus simple
    # Un total de 0 (ou négatif) ne demande aucune pièce.
    if total <= 0:
        return 0

    # ÉTAPE 2 : choisir une valeur qui veut dire "impossible"
    # Même avec seulement des pièces de 1, il faut au maximum
    # "total" pièces. Donc "total + 1" ne peut jamais être
    # une vraie réponse : on s'en sert comme marqueur.
    impossible = total + 1

    # ÉTAPE 3 : créer le tableau des réponses
    # pieces_minimum_pour[montant] contiendra le plus petit nombre
    # de pièces qu'il faut pour payer exactement ce montant.
    # "total + 1" cases, pour couvrir tous les montants de 0 à total.
    # Au départ, on ne sait payer aucun montant : tout vaut "impossible".
    pieces_minimum_pour = [impossible] * (total + 1)

    # Seule réponse connue d'avance : payer 0 demande 0 pièce.
    pieces_minimum_pour[0] = 0

    # ÉTAPE 4 : remplir le tableau, pièce par pièce
    for valeur_piece in coins:
        # On regarde chaque montant que cette pièce peut aider à payer.
        # On commence à "valeur_piece" : une pièce de 5 ne peut pas
        # servir à payer un montant plus petit que 5.
        for montant in range(valeur_piece, total + 1):
            # Si on utilise cette pièce, combien reste-t-il à payer ?
            reste_a_payer = montant - valeur_piece

            # Pièces nécessaires = pièces pour payer le reste + celle-ci.
            nombre_de_pieces = pieces_minimum_pour[reste_a_payer] + 1

            # Si c'est mieux que le record actuel, on le remplace.
            # (Si le reste était impossible, ce nombre est trop grand
            # et ne battra jamais le record : c'est voulu.)
            if nombre_de_pieces < pieces_minimum_pour[montant]:
                pieces_minimum_pour[montant] = nombre_de_pieces

    # ÉTAPE 5 : lire la réponse dans la case du total
    # Si elle vaut encore "impossible", aucune combinaison ne marche.
    if pieces_minimum_pour[total] == impossible:
        return -1

    # Sinon, elle contient le plus petit nombre de pièces possible.
    return pieces_minimum_pour[total]
