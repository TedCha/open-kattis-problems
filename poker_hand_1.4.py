# https://open.kattis.com/problems/pokerhand

# It's so ugly it's beautiful
string = input().replace(" ", "")[::2]; print(max(dict((letter, string.count(letter)) for letter in set(string)).values()))