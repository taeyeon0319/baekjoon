import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

def bfs(v):
    q= deque([v])
    array[v] = 1
    while q:
        v = q.popleft()
        if v==G:
            return array[v]-1
        for nv in (v+U, v-D):
            if 1<=nv<=F and not array[nv]:  # 이동 가능한 층인지 확인
                array[nv]=array[v]+1
                q.append(nv)
    if array[G]==0:
        return 'use the stairs'
        
array = [0] * (F+1) 

print(bfs(S))
