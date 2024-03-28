from collections import deque
n = int(input())
m = int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


# dfs로 풀기
# visited_dfs = [0]*(n+1)

# v=1
# cnt=0
# def dfs(v):
#     global cnt
#     visited_dfs[v]=1
#     for i in graph[v]:
#         if visited_dfs[i]==0:
#             dfs(i)
#             cnt+=1
# dfs(v)
# print(cnt)
    
visited_bfs = [0]*(n+1)
v =1
cnt = 0
def bfs(v):
    global cnt
    visited_bfs[v]=1
    q =deque([v])
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited_bfs[i]==0:
                visited_bfs[i]=1
                q.append(i)
                cnt+=1
bfs(v)
print(cnt)