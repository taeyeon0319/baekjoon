n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

#완전탐색 - 백트래킹으로 풀기
# answer = 0
# def dfs(day, income):
#     global answer
    
#     #[1] 종료조건 : 가능한 day을 종료에 관련된것으로 정의
#     if day>=n:
#         answer = max(answer, income)
#         return
    
#     #[2] 하부호출 : 화살표 개수만큼 호출
#     #상담하는 경우
#     if (day+schedule[day][0])<=n:
#         dfs(day+schedule[day][0], income+schedule[day][1])
#     #상담안하는 경우
#     dfs(day+1, income)

# dfs(0, 0) #n=0부터, 수익은 아직 0
# print(answer)


dp = [0]*(n+1)

for i in range(n-1, -1, -1): #역방향 진행
    if i+schedule[i][0] <= n:
        dp[i]=max(dp[i+schedule[i][0]]+schedule[i][1], dp[i+1])
    else:
        dp[i]=dp[i+1]

print(dp[0])