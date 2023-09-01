n = int(input())
result_score = 0
for _ in range(n):
    answer = int(input())
    if answer==1:
        result_score+=1
    
if result_score>(n//2):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")