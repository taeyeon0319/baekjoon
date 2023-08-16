import sys
input = sys.stdin.readline

n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

num.sort()

print(round(sum(num)/n))
print(num[(n-1)//2])

number = list(set(num))
mode = []
max_cnt = 0

for i in number:
    if max_cnt==num.count(i):
        mode.append(i)
    elif max_cnt < num.count(i):
        mode = []
        mode.append(i)
        max_cnt = num.count(i)
if len(mode)>1:
    mode.sort()
    print(mode[1])
else:
    print(mode[0])

print(max(num)-min(num))