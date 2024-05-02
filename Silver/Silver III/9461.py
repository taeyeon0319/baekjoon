import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n = int(input())
    dp = [1] * (n)

    if n<=3:
        print(1)
    elif n<=5:
        print(2)
    else:
        dp[3] = 2
        dp[4] = 2
        for i in range(5, n):
            dp[i] = dp[i-1]+dp[i-5]
        print(dp[n-1])
    
    