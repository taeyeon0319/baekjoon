n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

#상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 빨강(rx, ry), 파랑(bx, by) 초기 좌표 설정
for i in range(n):
    for j in range(m):
        if graph[i][j]=='R':
            rx, ry = i, j
        if graph[i][j]=='B':
            bx, by = i, j

def move(x, y, d):
    back=-1 
    for cnt in range(1, 10): #최대로 뻗어가서 벽을 만날때까지 진행
        nx, ny = x+dx[d]*cnt, y+dy[d]*cnt
        if graph[nx][ny]=='#': #벽을 만나면 그 전 단계까지니까 한칸 빼줘야함
            return cnt+back
        if graph[nx][ny]=='O': #구멍을 만나면 구멍에 들어가니까 cnt
            return cnt
        if graph[nx][ny]=='R' or graph[nx][ny]=='B': #다른 공이 있는 자리라면 한칸 빼줘야함
            back-=1



def dfs(n, rx, ry, bx, by):
    global ans
    if(n, rx, ry, bx, by) in v_set: #이미 이 시도횟수에 좌표조합을 해봄 => 가지치기!
        return
    v_set.add((n, rx, ry, bx, by)) # 안해본거라면 중복체크를 위해 표시
    
    if n>10:                        #10회 이하까지만 진행
        return 
    
    for d in range(4):              # 상하좌우로 구술 이동하기

        # [1] 각 공의 이동거리 계산
        r_cnt = move(rx, ry, d)     #해당방향으로 몇칸 갔는지 count
        b_cnt = move(bx, by, d)
        if r_cnt==0 and b_cnt==0:   #둘 다 이동을 안했다면
            continue                #해당 방향으로는 탐색할 필요 없음
        
        # [2] 각 공의 이동 반영
        nrx, nry = rx+dx[d]*r_cnt, ry+dy[d]*r_cnt #이동한 새 좌표 표시
        nbx, nby = bx+dx[d]*b_cnt, by+dy[d]*b_cnt

        # [3] 이동한 위치가 구멍인 경우 처리(성공/실패)
        if graph[nbx][nby]=='O':    #파란색 구슬이 구멍에 들어가면 실패
            continue
        else:
            if graph[nrx][nry]=='O':   #빨간색 구슬이 구멍에 들어가면 성공
                ans = min(ans, n)
                return
        
        # [4] 둘다 구멍이 아닌 경우(next좌표 기준으로 다음 시도)
        # 현재위치를 빈칸으로 하고 이동한 새 위치에 'R', 'B'구슬 표시
        graph[rx][ry], graph[bx][by]='.', '.'
        graph[nrx][nry], graph[nbx][nby]='R', 'B'

        dfs(n+1, nrx, nry, nbx, nby)

        graph[nrx][nry], graph[nbx][nby]='.', '.'
        graph[rx][ry], graph[bx][by]='R', 'B' #원상복구 해놓기
        


v_set = set() #해당 시도횟수 때 R, B 구슬좌표가 같다면 이미 해본 거임
ans = 11
dfs(1, rx, ry, bx, by)
if ans==11:
    ans=-1
print(ans)