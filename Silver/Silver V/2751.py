import sys
n = int(sys.stdin.readline())
num_list = []
for i in range(n):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()

for i in range(n):
    print(num_list[i])