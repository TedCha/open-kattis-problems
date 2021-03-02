# https://open.kattis.com/problems/kafkaesque

count = 1
previousClerkNumber = 0

n = int(input())
for i in range(n):
    clerkNumber = int(input())

    if previousClerkNumber > clerkNumber:
        count += 1
    
    previousClerkNumber = clerkNumber

print(count)