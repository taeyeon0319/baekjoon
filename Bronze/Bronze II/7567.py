plate = input()
result =10

for i in range(1, len(plate)):
    if plate[i]==plate[i-1]:
        result+=5
    else:
        result+=10
print(result)