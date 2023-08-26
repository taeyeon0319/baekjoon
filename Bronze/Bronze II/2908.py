a, b= input().split()
a_reverse = int(a[::-1])
b_reverse = int(b[::-1])

print(a_reverse if a_reverse>b_reverse else b_reverse)