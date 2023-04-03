import sys
n = int(sys.stdin.readline())
l = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    l.append((age, name))

l.sort(key=lambda x : x[0])

for i in l:
    print(i[0], i[1])

'''
람다(lambda)

a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]
sorted(a, key = lambda x : x[0])
==> a의 첫번째 숫자들을 기준으로 배열한다.
==> [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

'''
