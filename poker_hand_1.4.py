# https://open.kattis.com/problems/pokerhand

# It's so ugly it's beautiful
h = input()[::3]; print(max({c: h.count(c) for c in set(h)}.values()))

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
countByUniqueRank = {rank: ranksInHand.count(rank) for rank in uniqueRanks}
# Input: uniqueRanks == {A, K}
# Output: countByUniqueRank == {'A': 4, 'K': 1}

# Get the max value from all unique rank values
# .values() returns an object (<class 'dict_values'>: a Dictionary View Object)
# https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects <- Documentation
maxValue = max(countByUniqueRank.values())

print(maxValue)
"""

