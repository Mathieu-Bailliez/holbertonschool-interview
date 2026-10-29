#!/usr/bin/python3
"""Module that determines the fewest coins needed to meet a total."""


def makeChange(coins, total):
    """Return the fewest coins needed to meet total, or -1 if impossible."""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        coin_count += total // coin
        total %= coin
        if total == 0:
            return coin_count

    return -1
