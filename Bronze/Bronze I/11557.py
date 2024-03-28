t = int(input())
for _ in range(t):
    n = int(input())
    college = ""
    drinkmax = 0
    for _ in range(n):
        c, drink = input().split()
        drink = int(drink)
        if(drinkmax<drink):
            drinkmax=drink
            college=c
    print(college)