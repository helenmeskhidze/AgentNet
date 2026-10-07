from numpy import random
from setup import LANDSCAPE, LANDSCAPE_LENGTH, TEAM_SIZE
from climb import climb
from SoloAgent import run_solo

# reset the starting position (else trivial)
starting_pos = random.randint(LANDSCAPE_LENGTH)

def run_team(team):
    pos = int(starting_pos)
    total = 0
    stalled = 0   # consecutive members who failed at the current position
    team_memberID = 0

    while stalled < len(team):
        new_pos, gained = climb(team[team_memberID]["strategy"], pos)
        total += gained
        stalled = stalled + 1 if new_pos == pos else 1
        pos = new_pos
        team_memberID = (team_memberID + 1) % len(team)

    return total, pos

def build_teams(agents):
    ranked = sorted(agents,
                    key=lambda a: LANDSCAPE[a["final_pos"]]["value"],
                    reverse=True)
    best = ranked[0]
    picks = random.choice(len(agents), TEAM_SIZE, replace=False)

    return {
        "Bestest (4 copies of best)": [best] * TEAM_SIZE,
        "Best (top 4)": ranked[:TEAM_SIZE],
        "Random (4 random)": [agents[j] for j in picks],
    }

def run_all_teams(agents):
    results = {}
    for name, team in build_teams(agents).items():
        total, final_pos = run_team(team)
        results[name] = (total, final_pos, LANDSCAPE[final_pos]["value"])
    return results

if __name__ == "__main__":
    agents = run_solo()
    for name, (total, pos, value) in run_all_teams(agents).items():
        print("Team", name, "| winnings:", total, "| ended at", pos, "with value", value)