t = int(input())
for _ in range(t):
    ynum = knum = 0
    for _ in range(9):
        y, k = map(int, input().split())
        ynum+=y
        knum+=k
    if ynum>knum:
        print('Yonsei')
    elif ynum<knum:
        print('Korea')
    else:
        print('Draw')