origin = [1, 1, 2, 2, 2, 8]
dong = list(map(int, input().split()))

for i in range(6):
    print(origin[i]-dong[i], end=" ")
