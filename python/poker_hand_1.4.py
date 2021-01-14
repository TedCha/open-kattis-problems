# https://open.kattis.com/problems/pokerhand

"""
# Original:# It's so ugly it's beautiful
# string = input().replace(" ", "")[::2]; print(max(dict((letter, string.count(letter)) for letter in set(string)).values()))
"""

# It's actually pretty nice
h=input()[::3]; print(max([h.count(c) for c in set(h)]))

"""
# Explanation:
# Creates a string and then slices every 3 characters to get only the value of the card
ranksInHand = input()[::3]
# Input: AC AD AH AS KD
# Output: AAAAK
# Transformation: AC AD AH AS KD -> AAAAK

# Gets the unique ranks in hand
uniqueRanks = set(ranksInHand)
# Input: AAAAK
# Output: {A, K}

# Create a count of each unique rank in the hand
# .count() is a string method to count how many times a character appears in a string
uniqueRankCount = [ranksInHand.count(rank) for rank in uniqueRanks]
# Input: uniqueRanks == {A, K}
# Output: uniqueRankCount == [4, 1] 

# Get the max value from all unique rank values
maxValue = max(uniqueRankCount)

print(maxValue)
"""

