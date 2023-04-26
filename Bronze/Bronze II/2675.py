t = int(input())
for _ in range(t):
    a, b = input().split()
    a = int(a)
    text=""
    for i in b:
        text += a*i
    print(text)