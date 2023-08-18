import sys
input = sys.stdin.readline

n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

num.sort()

print(round(sum(num)/n))
print(num[(n-1)//2])

dic = dict()
for i in num:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

mx = max(dic.values())
mx_dic=[]

for i in dic:
    if mx==dic[i]:
        mx_dic.append(i)

if len(mx_dic)>1:
    print(mx_dic[1])
else:
    print(mx_dic[0])
# number = list(set(num))
# mode = []
# max_cnt = 0

# for i in number:
#     if max_cnt==num.count(i):
#         mode.append(i)
#     elif max_cnt < num.count(i):
#         mode = []
#         mode.append(i)
#         max_cnt = num.count(i)
# if len(mode)>1:
#     mode.sort()
#     print(mode[1])
# else:
#     print(mode[0])

print(max(num)-min(num))