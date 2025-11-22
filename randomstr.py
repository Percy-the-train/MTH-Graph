"""
Random strategy solver for two feedback types.

Run this file directly to test the random strategy on both feedback types.
Defaults to length=3 for quick visible output; change length to 4 for full run.
"""
import random
import time
from core import all_codes, classic_feedback, positional_feedback

def run_random_one_secret(feedback_fn, codes, secret):
    """Solve a single secret using a random-guess strategy (avoid repeat guesses in a run)."""
    candidates = set(codes)
    tried = set()
    guesses = 0

    while True:
        guesses += 1
        # choose a random candidate not yet tried if possible
        choices = [c for c in candidates if c not in tried]
        if not choices:
            choices = list(candidates)
        guess = random.choice(choices)
        tried.add(guess)

        fb = feedback_fn(secret, guess)
        # reduce candidates consistent with feedback
        candidates = {c for c in candidates if feedback_fn(c, guess) == fb}

        if guess == secret:
            return guesses

def test_random_strategy(length=3):
    codes = all_codes(length)
    total = len(codes)
    strategies_name = "Random"
    feedback_types = [
        ("Classic (Bulls/Cows)", classic_feedback),
        ("Positional (2/1/0)", positional_feedback),
    ]

    print(f"Random strategy: testing all {total} codes (length={length})")
    print("="*60)

    for fb_name, fb_fn in feedback_types:
        print(f"\nFEEDBACK TYPE: {fb_name}")
        print("-"*40)
        start = time.time()
        counts = []
        for i, secret in enumerate(codes):
            # progress dots
            if (i + 1) % (total // 20 or 1) == 0:
                print(".", end="", flush=True)
            steps = run_random_one_secret(fb_fn, codes, secret)
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
    test_random_strategy(length=3)