n = int(input())
for i in range(1, n+1):
    a = i+sum(map(int, str(i)))
    if a==n:
        print(i)
        break
    if i==n:
        print(0)