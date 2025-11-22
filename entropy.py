"""
Entropy strategy solver for two feedback types.

Run this file directly to test the entropy strategy on both feedback types.
Defaults to length=3 for quick visible output; change length to 4 for full run.
"""
import time
from core import all_codes, classic_feedback, positional_feedback, entropy_from_counts

def run_entropy_one_secret(feedback_fn, codes, secret):
    """Solve a single secret using an entropy-based selection among current candidates."""
    candidates = set(codes)
    tried = set()
    guesses = 0

    while True:
        guesses += 1

        if len(candidates) == 1:
            guess = next(iter(candidates))
        else:
            # Prefer evaluating guesses not yet tried in this run
            evaluation_pool = [g for g in candidates if g not in tried]
            if not evaluation_pool:
                evaluation_pool = list(candidates)

            best_guess = None
            best_score = -float('inf')
            for possible_guess in evaluation_pool:
                partition = {}
                for code in candidates:
                    fb = feedback_fn(code, possible_guess)
                    partition[fb] = partition.get(fb, 0) + 1
                score = entropy_from_counts(partition)
                if best_guess is None or score > best_score:
                    best_score = score
                    best_guess = possible_guess

            guess = best_guess

        tried.add(guess)
        fb = feedback_fn(secret, guess)
        candidates = {c for c in candidates if feedback_fn(c, guess) == fb}

        if guess == secret:
            return guesses

def test_entropy_strategy(length=3):
    codes = all_codes(length)
    total = len(codes)
    strategies_name = "Entropy"
    feedback_types = [
        ("Classic (Bulls/Cows)", classic_feedback),
        ("Positional (2/1/0)", positional_feedback),
    ]

    print(f"Entropy strategy: testing all {total} codes (length={length})")
    print("="*60)

    for fb_name, fb_fn in feedback_types:
        print(f"\nFEEDBACK TYPE: {fb_name}")
        print("-"*40)
        start = time.time()
        counts = []
        for i, secret in enumerate(codes):
            if (i + 1) % (total // 20 or 1) == 0:
                print(".", end="", flush=True)
            steps = run_entropy_one_secret(fb_fn, codes, secret)
            counts.append(steps)
        elapsed = time.time() - start
        avg = sum(counts) / total
        worst = max(counts)
        print(f" DONE ({elapsed:.2f}s)")
        print(f"    → Strategy : {strategies_name}")
        print(f"    → Average  : {avg:.3f} guesses")
        print(f"    → Worst    : {worst} guesses")

if __name__ == "__main__":
    # Quick default so you see output immediately. Set to 4 for the full 5040-code run.
    test_entropy_strategy(length=3)