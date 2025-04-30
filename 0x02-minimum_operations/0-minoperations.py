#!/usr/bin/python3
"""
This module provides a method to calculate the minimum number of operations
required to generate 'n' H characters using only Copy All and Paste operations.
"""

def minOperations(n):
    """
    Calculates the minimum number of operations to get exactly n H characters.
    
    Parameters:
        n (int): The target number of H characters.
        
    Returns:
        int: The minimum number of operations, or 0 if n is impossible to achieve.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

