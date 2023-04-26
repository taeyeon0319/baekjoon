t = int(input())
def cal(l):
    result=float(l[0])
    for i in range(1, len(l)):
        if l[i]=='@':
            result*=3
        elif l[i]=='%':
            result+=5
        elif l[i]=='#':
            result-=7
    
    return result

for _ in range(t):
    a_li= list(input().split())
    print("{:.2f}".format(cal(a_li)))
    