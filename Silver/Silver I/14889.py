N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
ans = 2147000000

def dfs(depth, idx):
    global ans
    if depth == N//2:
        a, b =0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    a+=graph[i][j]
                elif not visited[i] and not visited[j]:
                    b+=graph[i][j]
        ans=min(ans, abs(a-b))
    for i in range(idx, N):
        if not visited[i]:
            visited[i]=True
            dfs(depth+1, i+1)
            visited[i]=False


dfs(0, 0)
print(ans)