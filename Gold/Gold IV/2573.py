import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
year = 0


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0:
                if graph[nx][ny]!=0:
                    visited[nx][ny]=1
                    q.append((nx, ny))
                else:
                    water[x][y]+=1




while True:
    answer = []
    visited = [[0]*M for _ in range(N)]
    water = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if graph[i][j] !=0 and visited[i][j]==0:
                answer.append(bfs(i, j))
    
    for i in range(N):
        for j in range(M):
            graph[i][j]-=water[i][j]
            if graph[i][j]<0:
                graph[i][j]=0
    
    if len(answer)==0 or len(answer)>=2:
        break

    year+=1

print(year) if len(answer)>=2 else print(0)