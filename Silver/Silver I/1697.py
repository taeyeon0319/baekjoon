import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v==K:
            return array[v]
        for nv in (v-1, v+1, v*2):
            if 0<=nv<MAX and not array[nv]:
                array[nv]=array[v]+1
                q.append(nv)

MAX = 200000
array = [0]*MAX
print(bfs(N))
