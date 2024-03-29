n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if board[i][j]=='R':
            rx, ry = i, j
        if board[i][j]=='B':
            bx, by = i, j

def move(x, y, direction):
    back = -1
    for cnt in range(1, 10):
        nx, ny = x+dx[direction]*cnt, y+dy[direction]*cnt
        if board[nx][ny]=='#':
            return cnt+back
        if board[nx][ny]=='O':
            return cnt
        if board[nx][ny]=='R' or board[nx][ny]=='B':
            back-=1

def dfs(n, rx, ry, bx, by):
    global move_cnt

    if n>10:
        return 
    for d in range(4):
        r_cnt = move(rx, ry, d)
        b_cnt = move(bx, by, d)
        if r_cnt==0 and b_cnt==0:
            continue

        nrx, nry = rx+dx[d]*r_cnt, ry+dy[d]*r_cnt
        nbx, nby = bx+dx[d]*b_cnt, by+dy[d]*b_cnt

        if board[nbx][nby]=='O':
            continue
        else:
            if board[nrx][nry]=='O':
                move_cnt=min(move_cnt, n)
                return 
            
        board[rx][ry]=board[bx][by]='.'
        board[nrx][nry], board[nbx][nby]='R', 'B'
        
        dfs(n+1, nrx, nry, nbx, nby)

        board[nrx][nry]=board[nbx][nby]='.'
        board[rx][ry], board[bx][by]='R', 'B'


move_cnt = 11
dfs(1, rx, ry, bx, by)
if move_cnt>10:
    print(-1)
else:
    print(move_cnt)