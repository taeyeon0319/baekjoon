import sys
input = sys.stdin.readline

    
n = int(input())
print(n//125+n//25+n//5)

# 규칙찾기
# 1. 5나 10이 아닌 수는 팩토리얼이 0이 안나온다.
# 2. 5! = 120(1), 10! = 3628800(2) 15! = 13..000(3)
#    20! = 24..0000(4) 25! = 15..00000000(6)
#    30! = 26..0000000(7)
# 5의 배수로 0의 개수는 n//5 근데 5의 제곱배수인
# 25, 125의 경우(n이 500보다 작아서) 0이 추가된다.

# 다른 방법
# from math import factorial
# n = int(input())
# cnt =0
# fac = factorial(n)

# for i in str(fac)[::-1]:
#     if i!='0':
#         break
#     else:
#         cnt+=1
# print(cnt)

# 또다른 방법
# n = int(input())
# def zero_cnt(n):
#     cnt = 0
#     while n!=0:
#         n//=5
#         cnt+=n
#     return cnt
# print(zero_cnt(n))
