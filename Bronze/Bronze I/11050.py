n, k = map(int, input().split())
result = 1
y = 1
for i in range(k):
    result *= n-i

for j in range(1, k+1):
    y *= j

print(result//y)

