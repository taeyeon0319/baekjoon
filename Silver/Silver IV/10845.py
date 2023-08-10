import sys


def push(l, x):
    return l.append(x)


def pop(l):
    if len(l) != 0:
       print(l[0])
       l.pop(0)
    else:
       print(-1)

def size(l):
    print(len(l))
    
def empty(l):
    if(len(l)==0):
        print(1)
    else:
        print(0)
    
def front(l):
    if(len(l)!=0):
        print(l[0])
    else:
        print(-1)

def back(l):
    if(len(l)!=0):
        print(l[len(l)-1])
    else:
        print(-1)
    

input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
    order = input().split()
    if order[0]=='push':
        push(l, order[1])
    elif order[0]=='pop':
        pop(l)
    elif order[0]=='size':
        size(l)
    elif order[0]=='empty':
        empty(l)
    elif order[0]=='front':
        front(l)
    else:
        back(l)
