import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lan = [int(input()) for _ in range(k)]

start = 1
end = max(lan)

while start <= end:
    mid = (start+end)//2
    lines = 0
    for i in lan:
        lines += i // mid
    if lines >= n:
        start = mid+1
    else:
        end = mid-1
print(end)

#이해다시하기!!!
