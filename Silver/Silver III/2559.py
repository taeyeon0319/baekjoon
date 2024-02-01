import sys
input = sys.stdin.readline
n, k = map(int, input().split())
tem = list(map(int, input().split()))
result = [sum(tem[:k])]

for i in range(0, n-k):
    result.append(result[i]-tem[i]+tem[k+i])
print(max(result))