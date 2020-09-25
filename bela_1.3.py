domCardValues = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
regCardValues = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}

x = input().split(' ')
n, b = int(x[0]), x[1]

score = 0
for i in range (4*n):
    y = input()
    j, k = y[0], y[1]

    if k == b:
        score += domCardValues[j]
    else:
        score += regCardValues[j]

print(score)