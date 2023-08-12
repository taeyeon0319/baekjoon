import sys
input = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False
    else:
        for n in range(2, int(num**0.5) + 1):
            if num % n == 0:
                return False
        return True

m, n = map(int, input().split())
for i in range(m, n + 1):
    if isPrime(i):
        print(i)



# 에라토스테네스의 체 : 가장 대표적인 소수 판별 알고리즘
# 2부터 배수들을 지워나가는 방식
# 2는 소수 -> 2의 배수들 삭제
# 3은 소수 -> 3의 배수들 삭제
# 그다음 4는 삭제됐으므로 5는 소수 -> 5의 배수들 삭제


# 나의 답안 - 시간초과...ㅎ..
# import sys
# input = sys.stdin.readline

# m, n = map(int, input().split())

# for i in range(m, n+1):
#     for j in range(2, i):
#         if i%j==0:
#             break
#         if j==(i-1):
#             print(i)


