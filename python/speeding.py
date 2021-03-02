# https://open.kattis.com/problems/speeding

n = int(input())

previousDistance = 0
previousTime = 0

velocityList = []

for i in range(n):
    time, distance = map(int, input().split())

    milesTravelled = distance - previousDistance
    timePassed = time - previousTime

    if timePassed != 0:
        velocity = milesTravelled // timePassed
    else:
        velocity = 0
    
    velocityList.append(velocity)

    previousDistance = distance
    previousTime = time

print(max(velocityList))
