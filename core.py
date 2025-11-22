from itertools import permutations
import math

# Core: code generation and feedback functions used by both solver scripts.

def all_codes(length=4):
    digits = '0123456789'
    return [''.join(p) for p in permutations(digits, length)]

def classic_feedback(secret, guess):
    """Return (bulls, cows) for secret vs guess."""
    bulls = sum(a == b for a, b in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return (bulls, cows)

def positional_feedback(secret, guess):
    """
    Return positional feedback as a tuple of 2/1/0 values:
      2 -> correct digit in correct position
      1 -> digit exists in secret but in different position
      0 -> digit not in secret
    """
    result = []
    for i, d in enumerate(guess):
        if secret[i] == d:
            result.append(2)
        elif d in secret:
            result.append(1)
        else:
            result.append(0)
    return tuple(result)

def entropy_from_counts(counts):
    """Shannon entropy of the partition counts (dict-like)."""
    total = sum(counts.values())
    if total <= 1:
        return 0.0
    return -sum((c/total) * math.log2(c/total) for c in counts.values() if c > 0)