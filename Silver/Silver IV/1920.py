n= int(input())
an = list(map(int, input().split()))
m = int(input())
ams = list(map(int, input().split()))
an.sort()

for am in ams:
    lo=0
    hi=n-1
    isExit=False

    while lo<=hi:
        mid=(lo+hi)//2
        if am==an[mid]:
            isExit=True
            print("1")
            break
        elif am>an[mid]:
            lo=mid+1
        else: #am<an[mid]
            hi=mid-1
    if not isExit:
        print("0")
'''
이분탑색
lo, mid, hi
'''

'''
<처음에 쓴 답 - 시간초과>
n = int(input())
an = list(map(int, input().split()))
m = int(input())
am = list(map(int, input().split()))


for i in range(m):
    cnt=0
    for j in range(n):
        if am[i]==an[j]:
            print("1")
            break
        else:
            cnt+=1
    if cnt==5:
        print("0")
'''
