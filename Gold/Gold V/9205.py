import sys
from collections import deque
input = sys.stdin.readline

def bfs(si, sj, ei, ej):
    q = deque([(si, sj)])
    visited = [0]*n
    while q:
        ci, cj = q.popleft()
        if abs(ci-ei)+abs(cj-ej)<=1000:
            return 'happy'
        for i in range(n):
            if visited[i]==0:
                ni, nj = store[i]
                if abs(ci-ni)+abs(cj-nj)<=1000: #범위내에 있으면
                    q.append((ni, nj))
                    visited[i]=1
    
    return 'sad'

t = int(input())
for _ in range(t):
    n =int(input()) #맥주 파는 편의점 개수
    store = []
    si, sj = map(int, input().split())
    for _ in range(n):
        ti, tj = map(int, input().split())
        store.append((ti, tj))
    ei, ej = map(int, input().split())
    
    answer = bfs(si, sj, ei, ej)
    print(answer)