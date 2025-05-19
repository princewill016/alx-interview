#!/usr/bin/python3
"""
N Queens Problem Solver
Solves the N queens puzzle using backtracking algorithm.
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if placing a queen at board[row][col] is safe.
    
    Args:
        board: Current board state
        row: Row to place queen
        col: Column to place queen
        n: Size of the board
    
    Returns:
        True if safe, False otherwise
    """
    # Check this column on upper rows
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check upper diagonal on left side
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1
    
    # Check upper diagonal on right side
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1
    
    return True


def solve_nqueens(board, row, n, solutions):
    """
    Solve N Queens problem using backtracking.
    
    Args:
        board: Current board state (list where board[i] = col of queen in row i)
        row: Current row to place queen
        n: Size of the board
        solutions: List to store all solutions
    """
    # Base case: if all queens are placed
    if row == n:
        # Convert board representation to required format
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return
    
    # Try placing queen in each column of current row
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen
            board[row] = col
            
            # Recursively place queens in remaining rows
            solve_nqueens(board, row + 1, n, solutions)
            
            # Backtrack (no need to explicitly remove queen
            # as we'll overwrite it in next iteration)


def main():
    """Main function to handle command line arguments and solve N Queens."""
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Validate N is a number
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Initialize board and solutions
    board = [-1] * n  # board[i] = column of queen in row i
    solutions = []
    
    # Solve the N Queens problem
    solve_nqueens(board, 0, n, solutions)
    
    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
