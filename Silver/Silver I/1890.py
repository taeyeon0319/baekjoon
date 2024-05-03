import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):

        # 현재 탐색하는 좌표가 오른쪽 맨 끝 점이면 반복을 멈춘다.
        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            break

        if j+graph[i][j]<N:
            dp[i][j+graph[i][j]] += dp[i][j]
        if i+graph[i][j]<N:
            dp[i+graph[i][j]][j]+= dp[i][j]
        print(dp)