#!/usr/bin/python3
"""
Rotate 2D Matrix 90 degrees clockwise in-place
"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise in-place.
    
    Args:
        matrix: n x n 2D list representing the matrix
    
    Returns:
        None (modifies matrix in-place)
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
