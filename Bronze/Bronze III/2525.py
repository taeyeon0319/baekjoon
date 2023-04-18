import sys
h, m = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())

result = m+c

if result<60:
    print(h, result)
else:
    h += int(result/60)
    result %= 60
    if h>=24:
        h-=24
    print(h, result)