# https://open.kattis.com/problems/ptice

seqA = 'ABC'
seqB = 'BABC'
seqC = 'CCAABB'

countHash = {
    'Adrian': 0,
    'Bruno': 0,
    'Goran': 0
    }

_ = input()
line = input()

n = 0
a = 0
b = 0
c = 0
while n < len(line):
    if n % 3 == 0:
        a = 0
    if n % 4 == 0:
        b = 0 
    if n % 6 == 0:
        c = 0
    
    if line[n] == seqA[a]:
        countHash['Adrian'] += 1
    if line[n] == seqB[b]:
        countHash['Bruno'] += 1
    if line[n] == seqC[c]:
        countHash['Goran'] += 1

    n += 1
    a += 1
    b += 1
    c += 1

highest = max(countHash.values())

results = [key for key, value in countHash.items() if value == highest]

print(highest)
for j in results:
    print(j)

    