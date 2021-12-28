# data = open("input.txt").readlines()
# # copy the data to a list
# lst = [d.strip() for d in data]

# hardcoding in input:
player0 = 8
player1 = 10

score0 = 0
score1 = 0
dice = 1
player = 0
rolls = 0

while score0 < 1000 and score1 < 1000:
    movement = 0
    for i in range(3):
        movement += dice
        dice += 1
        rolls += 1
        if dice > 100:
            dice = 1
    # print movement
    if player == 0:
        player0 += movement - 1
        player0 = player0%10 + 1
        score0 += player0
    else:
        player1 += movement - 1
        player1 = player1%10 + 1
        score1 += player1
    player = (player + 1) % 2
    # print score0, score1

print min(score0, score1) * rolls