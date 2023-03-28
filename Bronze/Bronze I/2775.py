t = int(input())

for i in range(t):
    f = int(input()) #층
    h = int(input()) #호
    zero_f = [i for i in range(1, h+1)] #0층

    for k in range(0, f):
        for l in range(1, h):
            zero_f[l]+=zero_f[l-1]
    print(zero_f[h-1])