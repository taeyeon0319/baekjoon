while True:
    n = int(input())
    cnt=[]
    if n==-1:
        break
    for i in range(1, n):
        if n%i==0:
            cnt.append(i)
    if sum(cnt)==n:
        print('{} = {}'.format(n, ' + '.join(map(str, cnt))))
    else:
        print("{} is NOT perfect.".format(n))

