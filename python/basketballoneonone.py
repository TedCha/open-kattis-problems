# https://open.kattis.com/problems/basketballoneonone

gameRecord = input()
gameRecordLength = len(gameRecord)

pointsHash = {"A": 0, "B": 0}

for i in range(0, gameRecordLength, 2):
    record = gameRecord[i:i+2]
    player = record[0]
    points = int(record[1])

    pointsHash[player] += points

winner = max(pointsHash, key=lambda k: pointsHash[k])

print(winner)
