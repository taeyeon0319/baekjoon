h, m, s = map(int, input().split())
t = int(input())

s += t
m += s//60
h+=m//60
print(h%24, m%60, s%60)
'''
a, b, c = map(int, input().split())
d = int(input())

while d!=0:
    c+=1
    if c==60:
        c=0
        b+=1
        if b==60:
            b=0
            a+=1
            if a==24:
                a=0
    d-=1
print(a, b, c)
'''
