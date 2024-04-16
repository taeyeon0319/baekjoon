import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    x, y =map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

def bfs(v):
    q = deque([v])
    visited[v]=1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i]==0:
                q.append(i)
                visited[i]=visited[v]+1

bfs(a)
print(visited[b]-1)
