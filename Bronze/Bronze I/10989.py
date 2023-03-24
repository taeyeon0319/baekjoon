import sys
n = int(sys.stdin.readline())
l = [0]*10000 #10000개의 수를 담을 수 있는 배열 만듦

for i in range(n):
    a = int(sys.stdin.readline())
    l[a-1] +=1

for i in range(10000):
    if l[i]!=0:
        for j in range(l[i]):
            print(i+1)


'''
sort()를 사용하면 메모리가 초과되므로 주의할 것!!
아래와 같이 풀면 메모리가 초과된다.
n = int(input())
l = []
for i in range(n):
    num = int(input())
    l.append(num)
l.sort()

for j in range(n):
    print(l[j])

'''


# 반복문으로 여러줄을 입력받을 때는 input()사용시 시간초과가 발생할 수있다.
# https://wikidocs.net/33 기타 표준 라이브러리 공부!!!
'''
import sys
a = int(sys.stdin.readline())
a, b, c = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split())
data = [sys.stdin.readline().strip() for i in range(n)] #strip()은 문자열 맨 앞과 맨 끝의 공백문자 제거
'''