dots = list(map(int, input().split()))
dots_as = sorted(dots)
dots_de = sorted(dots, reverse=True)

if dots==dots_as:
    print("ascending")
elif dots==dots_de:
    print("descending")
else:
    print("mixed")