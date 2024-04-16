import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

q =deque()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if graph[i][j]!=0:
            q.append((i, j))
print(graph)
print(q)