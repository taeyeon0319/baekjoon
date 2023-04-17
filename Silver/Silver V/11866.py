n, k = map(int, input().split())
l = []
index = 0
result = []

for i in range(1, n+1):
    l.append(i)

while len(l)!=0:
    index += (k-1)
    index %= len(l)
    result.append(l.pop(index))
    
print("<", end="")
for i in range(len(result)-1):
    print(result[i], end=", ")
print("{}>".format(result[-1]))