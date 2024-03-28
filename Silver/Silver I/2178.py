from collections import deque
n, m =map(int, input().split())
graph=[]


for _ in range(n):
    graph.append(list(map(int, input())))
x=0
y=0
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx, ny))
    print(graph[n-1][m-1])
bfs(x, y)

