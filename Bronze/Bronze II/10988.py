s = input()
result = 1
for i in range(len(s)//2):
    if s[i]!=s[-i-1]:
        result=0
        break
print(result)