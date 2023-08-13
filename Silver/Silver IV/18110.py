import sys
input = sys.stdin.readline

def round2(num): #사사오입
    return int(num) + (1 if num-int(num)>=0.5 else 0)

n = int(input())
julsa = round2(n*0.15)
people = []

if n==0:
    print(0)
else:
    for _ in range(n):
        people.append(int(input()))
    people.sort()

    result = 0
    for i in range(julsa, n-julsa):
        result+=people[i]
    print(round2(result/(n-2*julsa)))

