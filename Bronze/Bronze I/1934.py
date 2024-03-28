import sys
input = sys.stdin.readline

t = int(input())

def gcd(x, y):
    r = x%y
    if r==0:
        return y
    return gcd(y, r)

for _ in range(t):
    a, b = map(int, input().split())
    print(a*b//gcd(a, b))

