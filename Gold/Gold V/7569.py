import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
q = deque()

def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0<=nx<H and 0<=ny<N and 0<=nz<M:
                if graph[nx][ny][nz]==0:
                    q.append((nx, ny, nz))
                    graph[nx][ny][nz]=graph[x][y][z] + 1

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k]==1:
                q.append((i, j, k)) #1인 위치를 전부 미리 큐에 담아놔야함

bfs()

max_days = 0
for a in range(H):
    for b in range(N):
        for c in range(M):
            if graph[a][b][c]==0:
                print(-1)
                exit()
            else:
                max_days = max(max_days, graph[a][b][c])
print(max_days-1)


