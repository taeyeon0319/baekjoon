def change(g):
    if g=='A+':
        return 4.5
    elif g=='A0':
        return 4.0
    elif g=='B+':
        return 3.5
    elif g=='B0':
        return 3.0
    elif g=='C+':
        return 2.5
    elif g=='C0':
        return 2.0
    elif g=='D+':
        return 1.5
    elif g=='D0':
        return 1.0
    else:
        return 0.0

result = 0
score_sum = 0
for _ in range(20):
    name, score, grade = input().split()
    score = float(score)
    if grade != 'P':
        result+= score*change(grade)
        score_sum += score

print(round(result/score_sum, 6))

    