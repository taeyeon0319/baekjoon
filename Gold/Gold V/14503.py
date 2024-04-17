import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

#북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0]*M for _ in range(N)]

count = 0
def bfs(x, y, d):
    global count
    q = deque([(x, y, d)])
    visited[x][y]=1
    count += 1
    while q:
        x, y, d = q.popleft()
        temp_d =d
        turn = 0 #회전횟수 
        for i in range(4):
            nd = (temp_d+3)%4
            nx = x+dx[nd]
            ny = y+dy[nd]
            temp_d = nd

            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny]==0 and visited[nx][ny]==0:
                    q.append((nx, ny, temp_d))
                    visited[nx][ny]=1
                    count+=1
                    break
                else:
                    turn +=1
            if turn==4: #네방향을 다 돌아봤으면 전으로
                bx = x + dx[(d+2)%4]
                by = y + dy[(d+2)%4]
                if graph[bx][by]==1:
                    return count
                q.append((bx, by, d))


# print(graph)
# print(visited)
bfs(r, c, d)
print(count)