# data = open("input.txt").readlines()
# # copy the data to a list
# lst = [d.strip() for d in data]

# hardcoding in input:
player0 = 8
player1 = 10


from functools import lru_cache # This is only available in Python3, I've been doing all the other ones on 2.7 so will need to switch workspace over to run this

# found this on a help guide for this problem, does memoization by caching response for function exec with same input
@lru_cache(maxsize=None)
def turn(player0, player1, score0, score1, playerTurn):
    if score0 >= 21:
        return 1, 0
    if score1 >= 21:
        return 0, 1

    wins0 = 0
    wins1 = 0
    # [3,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,9]
    dice = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    for roll in dice:
        rollTimes = dice[roll]
        newPlayer0 = player0
        newPlayer1 = player1
        newScore0 = score0
        newScore1 = score1
        newPlayerTurn = playerTurn
        if playerTurn == 0:
            newPlayer0 += roll - 1
            newPlayer0 = newPlayer0%10 + 1
            newScore0 += newPlayer0
        else:
            newPlayer1 += roll - 1
            newPlayer1 = newPlayer1%10 + 1
            newScore1 += newPlayer1
        newPlayerTurn = (newPlayerTurn + 1) % 2
        w0, w1 = turn(newPlayer0, newPlayer1, newScore0, newScore1, newPlayerTurn)
        wins0 += w0*rollTimes
        wins1 += w1*rollTimes
    return wins0, wins1

print(turn(player0, player1, 0, 0, 0))