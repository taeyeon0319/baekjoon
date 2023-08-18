import sys
input = sys.stdin.readline

x = list(map(int, input().split()))
result = 0
for i in x:
    result+=i**2

print(result%10)