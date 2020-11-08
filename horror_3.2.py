n, h, l = [int(x) for x in input().split()]
horrorList = {int(key): 0 for key in input().split()}

# Create rest of movies not included in intial horror list
# and set their value to None
for i in range(n):
    if i not in horrorList:
        horrorList[i] = None

for j in range(l):
    a, b = [int(x) for x in input().split()]
    
    if horrorList[a] != None and horrorList[b] != None:
        if horrorList[a] == horrorList[b]:
            horrorList[a] += 1
            horrorList[b] += 1
        #elif horrorList[a]
    elif horrorList[a] == None and horrorList[b] == None:
        continue
    elif horrorList[a] == None:
        horrorList[a] = horrorList[b] + 1
    elif horrorList[b] == None:
        horrorList[b] = horrorList[a] + 1

# Set all values that are stil None to the highest value
for key, value in horrorList.items():
    if horrorList[key] == None:
        horrorList[key] = n

# Get the max value in the horror list.
highest = max(horrorList.values())

# Check if there's multiple answers and print the min
print(min([key for key, value in horrorList.items() if value == highest]))
    