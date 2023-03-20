t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    y = 0
    x = 1

    for i in range(n):
        if y>=h:
            y = 0
            x += 1
        y += 1

    if x<10:
        print("{}0{}".format(y, x))
    else:
        print("{}{}".format(y, x))
