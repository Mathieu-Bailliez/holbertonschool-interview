#!/usr/bin/python3
"""
Module for determining if all lockboxes can be opened.
"""


def canUnlockAll(boxes):
	"""
	Determines if all boxes can be opened.

	Args:
		boxes (list): A list of lists containing keys.

	Returns:
		bool: True if all boxes can be opened, otherwise False.
	"""
	n = len(boxes)
	opened = set([0])
	keys = [0]

	while keys:
		current = keys.pop()

		for key in boxes[current]:
			if key < n and key not in opened:
				opened.add(key)
				keys.append(key)

	return len(opened) == n



canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
