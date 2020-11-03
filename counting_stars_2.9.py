# https://open.kattis.com/problems/countingstars

from collections import deque
from sys import stdin

caseCount = 0

for line in stdin:

    caseCount += 1
    x, y = [int(x) for x in line.split()]
    graph = [input() for _ in range(x)]
    starCount = 0
    visited = set()

    def validMoves(node):
        r, c = node[0], node[1]

        validMoves = []

        for move in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
            y, x = move[0], move[1]
            if not (0 <= x < len(graph[0])) or not (0 <= y < len(graph)):
                continue
            else:
                if graph[y][x] == "-":
                    validMoves.append(move)
        return validMoves

    def breadthFirstSearch(node):
        queue = deque([node])
        visited.add(node)

        while queue:
            node = queue.popleft()
            for move in validMoves(node):
                if move not in visited:
                    queue.append(move)
                    visited.add(move)
            
    for k in range(len(graph)):
        for j in range(len(graph[k])):
            currentNode = (k, j)
            if (graph[k][j] == "-") and (currentNode not in visited):
                breadthFirstSearch(currentNode)
                starCount += 1

    print(f"Case {caseCount}: {starCount}")