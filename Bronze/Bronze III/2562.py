num_list=[]
for _ in range(9):
    num_list.append(int(input()))
idx=1

for num in num_list:
    if num==max(num_list):
        break
    else:
        idx+=1
print(max(num_list))
print(idx)