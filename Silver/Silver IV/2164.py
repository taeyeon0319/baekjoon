import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for i in range(n):
    q.append(i+1)
while len(q)>1:
    q.popleft()
    q.append(q.popleft())
print(q.pop())
'''
<python-Deque(덱)>
- 데이터 값을 저장하는 기본적인 구조, 일차원적인 선형 자료구조
- 스택과 큐를 모두 지원
'''

'''
<내 답안 -- 시간 초과 나옴>
n = int(input())
num_list=[i for i in range(1, n+1)]

while len(num_list)>1:
    num_list.pop(0)
    a = num_list[0]
    num_list.pop(0)
    num_list.append(a)
    
print(num_list[0])
'''
