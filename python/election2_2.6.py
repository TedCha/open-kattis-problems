# https://open.kattis.com/problems/election2

n = int(input())

candidatesByParty = {}

for i in range(n):
    candidate = str(input())
    party = str(input())

    candidatesByParty[candidate] = party

candidatesByVotes = dict.fromkeys(candidatesByParty, 0)

m = int(input())

for j in range(m):
    candidate = str(input())
    
    # Very tricky OpenKattis
    if candidate not in candidatesByVotes:
        candidatesByVotes[candidate] = 0
        candidatesByParty[candidate] = 'independent'

    candidatesByVotes[candidate] += 1

highest = max(candidatesByVotes.values())

results = [key for key, value in candidatesByVotes.items() if value == highest]

if len(results) > 1:
    print('tie')
else:
    print(candidatesByParty[results[0]])
