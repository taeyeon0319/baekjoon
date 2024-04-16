import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*(N) for _ in range(N)]

result = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global count
    visited[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if graph[nx][ny]==1 and visited[nx][ny]==0:
                dfs(nx, ny)
                count+=1

for i in range(N):
    for j in range(N):
        if graph[i][j]==1 and visited[i][j]==0:
            count = 1
            dfs(i, j)
            result.append(count)

result.sort()
print(len(result))
for v in result:
    print(v)
