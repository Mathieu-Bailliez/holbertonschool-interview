#!/usr/bin/python3
"""Determine whether all boxes in a list can be unlocked."""


def canUnlockAll(boxes):
    """Take a list of list as a parameter and return True if the all the boxe
    can be unlocked and False if not"""

    n = len(boxes)

    unlocked = {0}

    keys = list(boxes[0])

    while keys:
        current_key = keys.pop()

        if current_key < n and current_key not in unlocked:
            unlocked.add(current_key)
            keys.extend(boxes[current_key])

    return len(unlocked) == n
