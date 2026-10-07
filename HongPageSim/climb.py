from setup import LANDSCAPE, LANDSCAPE_LENGTH, VERBOSE

def climb(strategy, pos, verbose=VERBOSE):
    """Move until a full pass finds nothing better. Returns (final_pos, gained)."""
    n = len(strategy)
    i = 0         # which strategy element to try next
    misses = 0    # consecutive checks with no improvement
    gained = 0

    while misses < n:
        candidate = (pos + strategy[i]) % LANDSCAPE_LENGTH

        if LANDSCAPE[candidate]["value"] > LANDSCAPE[pos]["value"]:
            if verbose:
                print("Moving from", pos, "to", candidate,
                      "with value", LANDSCAPE[candidate]["value"])
            pos = candidate
            gained += LANDSCAPE[pos]["value"]
            misses = 0
        else:
            misses += 1

        i = (i + 1) % n

    return pos, gained