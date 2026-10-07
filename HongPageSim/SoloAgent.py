import copy
from setup import AGENTS, starting_pos, LANDSCAPE
from climb import climb

def run_solo():
    agents = copy.deepcopy(AGENTS)   # fresh winnings each call
    for agent in agents:
        agent["final_pos"], agent["winnings"] = climb(agent["strategy"], int(starting_pos))
    return agents

if __name__ == "__main__":
    agents = run_solo()
    best = max(agents, key=lambda a: a["winnings"])
    print("Max winnings acrued:", best["winnings"], "with strategy", best["strategy"])


    a, best_stop = max(enumerate(agents), key=lambda t: LANDSCAPE[t[1]["final_pos"]]["value"])
    print("Agent", a, "has the best stop: position", best_stop["final_pos"],
          "with value", LANDSCAPE[best_stop["final_pos"]]["value"],
          "and strategy", best_stop["strategy"])