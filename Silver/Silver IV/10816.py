#이분탐색
import sys

def binary_search(l, target, start, end):
    if start > end:
        return 0
    mid = (start+end)//2

    if l[mid] == target:
        return count.get(target)
    elif l[mid]<target:
        return binary_search(l, target, mid+1, end)
    else:
        return binary_search(l, target, start, mid-1)
    

input = sys.stdin.readline
n = int(input())
cards = sorted(list(map(int, input().split())))

m = int(input())
candidate = list(map(int, input().split()))

count = {}

for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card]=1

for target in candidate:
    print(binary_search(cards, target, 0, len(cards)-1), end=" ")

'''
줄바꿈 없이 출력
print(result[i], end=" ")


<내 풀이 - 시간초과>
n = int(input())
card = list(map(int, input().split()))

m = int(input())
card2 = list(map(int, input().split()))

result=[]

for i in range(m):
    test = 0
    for j in range(n):
        if card[j]==card2[i]:
            test+=1
    result.append(test)

for i in range(m):
    print(result[i], end=" ")
'''
