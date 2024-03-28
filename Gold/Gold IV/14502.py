n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if graph[nx][ny]==0:
            graph[nx][ny]=1
        if graph[nx][ny]==2:
            dfs(nx, ny)
dfs(0, 0)
dfs(1, 5)
print(graph)