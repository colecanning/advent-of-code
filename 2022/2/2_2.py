from strategy import strategy

rounds = strategy.split('\n')

print(rounds)


ROCK2 = 'A'
PAPER2 = 'B'
SCISSORS2 = 'C'

ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'


WIN = 'Z'
LOSE = 'X'
DRAW = 'Y'

score_map = {
    WIN: {
        ROCK2: PAPER,
        PAPER2: SCISSORS,
        SCISSORS2: ROCK,
    },
    LOSE: {
        ROCK2: SCISSORS,
        PAPER2: ROCK,
        SCISSORS2: PAPER,
    },
    DRAW: {
        ROCK2: ROCK,
        PAPER2: PAPER,
        SCISSORS2: SCISSORS,
    },
}

chosen_score_map = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

outcome_score_map = {
    WIN: 6,
    LOSE: 0,
    DRAW: 3
}


score = 0
for round in rounds:
    p1, _, p2 = round
    to_play = score_map[p2][p1]
    score += outcome_score_map[p2]
    score += chosen_score_map[to_play]

print(score)