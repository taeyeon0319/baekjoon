t = int(input())
a = 60*5
b = 60*1
c = 10

a_cnt = t//a
b_cnt = (t%a)//b
c_cnt = (t%a%b)//c

if t%a%b%c!=0:
    print(-1)
else:
    print(a_cnt, b_cnt, c_cnt)
