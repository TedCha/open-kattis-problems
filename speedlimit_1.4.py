#https://open.kattis.com/problems/speedlimit

while True:
    n = int(input())
    if n == -1:
        break

    travelLog = []
    totalTime = 0

    for i in range(0, n):
        mph, hours = [int(x) for x in input().split()]
        if travelLog:
            x = travelLog[i-1][1]
        else:
            x = 0
        
        travelLog.append((mph, hours))

        totalTime += mph * (hours - x)
    print(f"{totalTime} miles")