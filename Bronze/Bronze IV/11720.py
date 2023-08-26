n = int(input())
n_list = list(map(int, input()))
result=0
for i in range(n):
    result+=n_list[i]
print(result)