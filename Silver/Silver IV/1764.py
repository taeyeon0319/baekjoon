import sys
input = sys.stdin.readline
n, m = map(int, input().split())
name_dict = {}
for _ in range(n):
    name=input().rstrip()
    name_dict[name]=1
for _ in range(m):
    name_s = input().rstrip()
    if name_s in name_dict:
        name_dict[name_s]+=1
    else:
        name_dict[name_s]=1
result=[]
for i in name_dict:
    if name_dict[i]==2:
        result.append(i)
result.sort()
print(len(result))
for r in result:
    print(r)
