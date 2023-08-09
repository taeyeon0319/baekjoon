n, m = map(int, input().split())

board = []
result=[]

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        result_W = 0 #시작점이 흰색일때
        result_B = 0 #시작점이 검은색일때

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2==0: #행/열 합이 짝수면(시작점과 같은 색)
                    if board[a][b]!='W': #시작점과 같은 색(W)이 아니면
                        result_W+=1
                    if board[a][b]!='B': #시작점과 같은 색(B)이 아니면
                        result_B+=1
                else:
                    if board[a][b]!='B':
                        result_W+=1
                    if board[a][b]!='W':
                        result_B+=1

        result.append(result_W)
        result.append(result_B)
print(min(result))
