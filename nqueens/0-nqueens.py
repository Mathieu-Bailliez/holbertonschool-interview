#!/usr/bin/python3
"""Solves the N queens problem using backtracking."""
import sys


def n_not_valid():
    """Check that N is a valid integer >= 4."""
    global N
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        return True
    if N < 4:
        print("N must be at least 4")
        return True
    return False


def is_safe(board, current_row, current_col):
    """Check if a queen can be placed at (current_row, current_col)."""
    for queen in board:
        queen_row = queen[0]
        queen_col = queen[1]

        if queen_col == current_col:
            return False
        if abs(queen_row - current_row) == abs(queen_col - current_col):
            return False
    return True


def solve_nqueens(row, n, board):
    """Place queens row by row and print every valid solution."""
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve_nqueens(row + 1, n, board)
            board.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if n_not_valid():
        sys.exit(1)
    solve_nqueens(0, N, [])
