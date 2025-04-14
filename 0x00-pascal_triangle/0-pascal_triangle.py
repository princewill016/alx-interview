#!/usr/bin/python3
"""
Module for Pascal's Triangle function
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    
    Args:
        n (int): The number of rows to generate
        
    Returns:
        list: Empty list if n <= 0, otherwise a list of lists representing Pascal's triangle
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # First row is always [1]
    
    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        prev_row = triangle[i-1]
        
        # Calculate middle elements (sum of the two numbers above)
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
        
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)
    
    return triangle
