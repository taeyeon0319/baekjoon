import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, t):
    visited[x][y]=1
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny]==0 and graph[nx][ny]>t:
                    visited[nx][ny]=1
                    q.append((nx, ny))

max_result = 0
for x in range(max(map(max, graph))+1):
    visited = [[0] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0 and graph[i][j]>x:
                bfs(i, j, x)
                count+=1

    max_result = max(max_result, count)

print(max_result)
