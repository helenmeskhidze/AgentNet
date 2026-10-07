from collections import Counter
from setup import N_RERUNS
from SoloAgent import run_solo
from SingleRoundTeams import run_all_teams

if __name__ == "__main__":
    agents = run_solo()   # fixed, so run once outside the loop
    wins = Counter()

    for _ in range(N_RERUNS):
        results = run_all_teams(agents)
        top_value = max(r[2] for r in results.values())
        for name, r in results.items():
            if r[2] == top_value:
                wins[name] += 1   # tied teams all get credit
 
    print("Wins out of", N_RERUNS, "reruns (best final position):")
    for name, count in wins.items():
        print(" ", name, ":", count)