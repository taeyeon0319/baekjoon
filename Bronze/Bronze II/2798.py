n, m=map(int, input().split())
num = list(map(int, input().split()))

result=0

num.sort(reverse=True)

for i in range(n):
    for k in range(i+1, n):
        for j in range(k+1, n):
            if num[i]+num[j]+num[k]>m:
                continue
            else:
                result = max(result, num[i]+num[j]+num[k])

print(result)
