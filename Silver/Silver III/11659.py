import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
p_sum = [0]
temp = 0

for i in num_list:
    temp += i
    p_sum.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    print(p_sum[j]-p_sum[i-1])
    