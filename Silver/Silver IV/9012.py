t = int(input())
for _ in range(t):
    s = list(input())
    check=0
    for i in s:
        if i=='(':
            check+=1
        elif i==")":
            check-=1
        if check<0:
            print("NO")
            break
    if check==0:
        print("YES")
    elif check>0:
        print("NO")