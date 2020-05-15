#import math module (standard library)
import math

#create coordinate list
coordList = [(0,2), (1,2), (2,2), (0,1), (1,1), (2,1), (0,0), (1,0), (2,0)]

#get input for all three lines and split it by space into a list
s1 = input().split(" ")
s2 = input().split(" ")
s3 = input().split(" ")

#join lists into one main list
fs = s1 + s2 + s3

#use map function to turn all list values from str to int
fs = list(map(int, fs))

#create new empty list
cl = []

#append the new list with each iteration of value from the 
#joined list and the coord list 
for i in range(0, len(fs)):
  cl.append([fs[i], coordList[i]])

#sort cl list in chronological numerical order
cl.sort()

#create a distance function to calculate length
#pass x1, x2, y1, y2 arguments
def distFunc(x1, x2, y1, y2):
  #use the sqrt function from math module and return the length
  dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
  return dist

#create variable equal to zero
f = 0
#for i in range of length of fs - 1 (8)
#pass the correct nested list value into dist function
for i in range(0, 8):
  j = distFunc(cl[i][1][0], cl[i + 1][1][0], cl[i][1][1], cl[i + 1][1][1])
  #f = f + j in each iteration
  f += j

#print solution
print(f)
