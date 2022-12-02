from strategy import strategy

rounds = strategy.split('\n')

print(rounds)


ROCK2 = 'A'
PAPER2 = 'B'
SCISSORS2 = 'C'

ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'

score_map = {
    ROCK: {
        ROCK2: 3,
        PAPER2: 0,
        SCISSORS2: 6,
    },
    PAPER: {
        ROCK2: 6,
        PAPER2: 3,
        SCISSORS2: 0,
    },
    SCISSORS: {
        ROCK2: 0,
        PAPER2: 6,
        SCISSORS2: 3,
    },
}

chosen_score_map = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}


score = 0
for round in rounds:
    p1, _, p2 = round
    score += score_map[p2][p1]
    score += chosen_score_map[p2]

print(score)