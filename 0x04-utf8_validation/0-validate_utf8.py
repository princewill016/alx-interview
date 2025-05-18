#!/usr/bin/python3
"""
Function to validate UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes (0-255)

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise
    """
    n_bytes = 0

    for num in data:
        byte = num & 0xFF  # Only consider the least significant 8 bits

        if n_bytes == 0:
            # Count leading 1s to determine byte length
            mask = 0x80
            while mask & byte:
                n_bytes += 1
                mask >>= 1

            # 1-byte char or invalid length
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check for continuation byte (10xxxxxx)
            if not (byte & 0x80 and not (byte & 0x40)):
                return False

        n_bytes = n_bytes - 1 if n_bytes else 0

    return n_bytes == 0

