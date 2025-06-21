#!/usr/bin/python3
"""
This module defines the island_perimeter function
which calculates the perimeter of an island represented
in a grid.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the grid.

    Args:
        grid (list of list of int): 2D grid representing the map.
            0 represents water, 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Check upper neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Shared edge with upper neighbor

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Shared edge with left neighbor

    return perimeter

