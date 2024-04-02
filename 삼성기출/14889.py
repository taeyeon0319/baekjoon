N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

M = N//2
answer = 100*N*M

def cal(a, b):
    asum = bsum = 0
    for i in range(M):
        for j in range(M):
            asum += graph[a[i]][a[j]]
            bsum += graph[b[i]][b[j]]
    return abs(asum-bsum)

def dfs(number, alist, blist):
    global answer
    #가지치기 : 이미 answer가 0이면 더 줄일 가능성 없음!
    if answer == 0 :
        return 
    
    if number==N:
        if len(alist)==len(blist):
            answer = min(answer, cal(alist, blist))
        print(alist)
        print(blist)
        print()
        return 
    dfs(number+1, alist+[number], blist)
    dfs(number+1, alist, blist+[number])

dfs(0, [], [])
print(answer)