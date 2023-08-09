n = int(input())
score=list(map(int, input().split()))

max_score = max(score)

result = 0
for i in range(n):
    result+= score[i]/max_score*100
print(result/n)

