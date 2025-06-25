#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine the winner of each round of the prime game.
    
    Args:
        x: number of rounds
        nums: array of n values for each round
    
    Returns:
        Name of player who won most rounds, or None if tie
    """
    if not nums or x <= 0:
        return None
    
    # Precompute prime counts up to max(nums) using Sieve of Eratosthenes
    max_n = max(nums)
    prime_counts = [0] * (max_n + 1)
    
    # Sieve to find all primes up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    
    # Count primes up to each number
    count = 0
    for i in range(max_n + 1):
        if is_prime[i]:
            count += 1
        prime_counts[i] = count
    
    # Determine winner for each round
    maria_wins = 0
    ben_wins = 0
    
    for i in range(x):
        if i < len(nums):
            n = nums[i]
            # Maria wins if odd number of primes, Ben wins if even
            if prime_counts[n] % 2 == 1:
                maria_wins += 1
            else:
                ben_wins += 1
    
    # Return overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Test with the provided example
if __name__ == "__main__":
    # Test case: x = 3, nums = [4, 5, 1]
    result = isWinner(3, [4, 5, 1])
    print(f"Winner: {result}")
    
    # Let's trace through each round:
    print("\nRound analysis:")
    
    # Round 1: n = 4
    # Primes ≤ 4: [2, 3] = 2 primes (even) → Ben wins
    print("Round 1 (n=4): Primes [2, 3] = 2 primes (even) → Ben wins")
    
    # Round 2: n = 5  
    # Primes ≤ 5: [2, 3, 5] = 3 primes (odd) → Maria wins
    print("Round 2 (n=5): Primes [2, 3, 5] = 3 primes (odd) → Maria wins")
    
    # Round 3: n = 1
    # Primes ≤ 1: [] = 0 primes (even) → Ben wins
    print("Round 3 (n=1): Primes [] = 0 primes (even) → Ben wins")
    
    print(f"\nBen wins 2/3 rounds, so Ben is the overall winner")
