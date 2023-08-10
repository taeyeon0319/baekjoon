import sys
input = sys.stdin.readline

n = int(input())
deque = []

for _ in range(n):
    order = input().split()
    if order[0]=='push_front':
        deque.insert(0, order[1])
    elif order[0]=='push_back':
        deque.append(order[1])
    elif order[0]=='pop_front':
        if len(deque)!=0:
            print(deque[0])
            deque.pop(0)
        else:
            print(-1)
    elif order[0]=='pop_back':
        if len(deque)!=0:
            print(deque[len(deque)-1])
            deque.pop(len(deque)-1)
        else:
            print(-1)
    elif order[0]=='size':
        print(len(deque))
    elif order[0]=='empty':
        if len(deque)!=0:
            print(0)
        else:
            print(1)
    elif order[0]=='front':
        if len(deque)!=0:
            print(deque[0])
        else:
            print(-1)
    else:
        if len(deque)!=0:
            print(deque[len(deque)-1])
        else:
            print(-1)