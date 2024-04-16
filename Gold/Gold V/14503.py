import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [-1,1, 0, 0]

