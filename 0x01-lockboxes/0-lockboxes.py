#!/usr/bin/python3
"""
0-can_unlock_all.py

Determine if all boxes can be opened given the keys in each box.

Boxes are numbered from 0 to n-1. boxes[0] is initially unlocked.
Each boxes[i] is a list of keys (integers) that can open other boxes.
A key with number k opens box k. Keys may not correspond to any box.
"""

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of list of int): Each index i represents a box;
                                     boxes[i] is the list of keys it contains.

    Returns:
        bool: True if every box from 0 to len(boxes)-1 can be opened; False otherwise.
    """
    n = len(boxes)
    # Track which boxes have been opened
    opened = set([0])
    # Stack of keys we have to use (initialize with keys in box 0)
    stack = [k for k in boxes[0] if 0 <= k < n]

    while stack:
        key = stack.pop()
        if key not in opened:
            opened.add(key)
            # Add any new keys found in this newly opened box
            for next_key in boxes[key]:
                if 0 <= next_key < n and next_key not in opened:
                    stack.append(next_key)

    return len(opened) == n


if __name__ == "__main__":
    # Example usage and simple test
    sample_boxes = [[1, 3], [3, 0, 1], [2], [0]]
    print(canUnlockAll(sample_boxes))  # Expected: False
    sample_boxes2 = [[1, 2], [2, 3], [3], []]
    print(canUnlockAll(sample_boxes2))  # Expected: True

