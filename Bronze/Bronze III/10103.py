n = int(input())
cnum = snum =100
for _ in range(n):
    c, s = map(int, input().split())
    if c>s:
        snum-=c
    elif c<s:
        cnum-=s
print(cnum)
print(snum)
