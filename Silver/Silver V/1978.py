n = int(input())
num = list(map(int, input().split()))
cnt = 0

for i in range(n):
    test = 0 
    if num[i]==2:
        cnt+=1

    elif num[i]!=1:
        for j in range(2, num[i]):
            if num[i]%j==0:
                break
            test+=1
        if test==num[i]-2:
            cnt+=1

print(cnt)
