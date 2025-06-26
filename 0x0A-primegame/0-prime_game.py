#!/usr/bin/python3
"""
Prime Game - Maria vs Ben
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game.
    
    Args:
        x: number of rounds
        nums: array of n values for each round
    
    Returns:
        Name of player who won most rounds, or None if tie
    """
    if not nums or x <= 0:
        return None
    
    # Find the maximum n to generate primes up to that limit
    max_n = max(nums)
    
    # Generate primes using Sieve of Eratosthenes
    def sieve_of_eratosthenes(limit):
        """Generate all primes up to limit using sieve method"""
        if limit < 2:
            return []
        
        # Create boolean array and initialize all entries as True
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        
        p = 2
        while p * p <= limit:
            if is_prime[p]:
                # Update all multiples of p
                for i in range(p * p, limit + 1, p):
                    is_prime[i] = False
            p += 1
        
        # Collect all prime numbers
        primes = []
        for i in range(2, limit + 1):
            if is_prime[i]:
                primes.append(i)
        
        return primes
    
    # Get all primes up to max_n
    primes = sieve_of_eratosthenes(max_n)
    
    # For each possible n, precompute the number of primes <= n
    prime_count = [0] * (max_n + 1)
    prime_idx = 0
    
    for n in range(1, max_n + 1):
        prime_count[n] = prime_count[n - 1]
        if prime_idx < len(primes) and primes[prime_idx] == n:
            prime_count[n] += 1
            prime_idx += 1
    
    # Count wins for each player
    maria_wins = 0
    ben_wins = 0
    
    for i in range(x):
        n = nums[i]
        # Number of primes <= n determines the winner
        # If odd number of primes, Maria wins (she goes first)
        # If even number of primes, Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
