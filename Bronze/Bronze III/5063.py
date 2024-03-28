import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    r, e, c = map(int, input().split())
    p = e-c
    if r<p:
        print("advertise")
    elif r>p:
        print("do not advertise")
    else:
        print("does not matter")