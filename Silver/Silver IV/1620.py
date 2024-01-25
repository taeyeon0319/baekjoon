import sys
input = sys.stdin.readline
n, m = map(int, input().split())
poketmon_dict = {}
for i in range(n):
    name = input().rstrip()
    poketmon_dict[i+1]=name
    poketmon_dict[name]=i+1
for _ in range(m):
    check = input().rstrip()
    if check.isdigit():
        print(poketmon_dict[int(check)])
    else:
        print(poketmon_dict[check])