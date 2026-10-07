import numpy as np
from numpy import random

LANDSCAPE_LENGTH = 1000
NUM_AGENTS = 100
MAX_STEP = 20
STRATEGY_LENGTH = 4
TEAM_SIZE = 4
VERBOSE = False 
N_RERUNS = 100
#random.seed(42)

LANDSCAPE = [
    {"location": i, 
     "value": random.randint(100)}
    for i in range(LANDSCAPE_LENGTH)
]

AGENTS = [
    {"strategy": [], "winnings": 0}
    for _ in range(NUM_AGENTS)
]

for agent in AGENTS:
    strategy = random.choice(range(1, MAX_STEP + 1), STRATEGY_LENGTH, replace=False)
    agent["strategy"] = sorted(strategy.tolist())

starting_pos = random.randint(LANDSCAPE_LENGTH)

if VERBOSE:
    print("Landscape is",LANDSCAPE)
    print("Agents are", AGENTS)
    print("Starting position is:",starting_pos, "with value", LANDSCAPE[starting_pos]["value"])
