row = 0
col = 0
max_num = 0
for i in range(1, 10):
    num = list(map(int, input().split()))
    
    if max_num<=max(num):
        max_num=max(num)
        row = i
        col = num.index(max(num))+1
print(max_num)
print(row, col)