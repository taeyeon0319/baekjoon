n = int(input())
T = [0]*(n)
P = [0]*(n)

for i in range(n):
    t, p = map(int, input().split())
    T[i]=t
    P[i]=p

dp = [0]*(n+1)

for i in range(n-1, -1, -1):
    if i+T[i]<=n:
        dp[i]=max(dp[i+1], dp[i+T[i]]+P[i])
    else:
        dp[i]=dp[i+1]

print(dp[0])