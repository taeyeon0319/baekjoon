n = int(input())
q1=q2=q3=q4=a = 0

for _ in range(n):
    x, y = map(int, input().split())
    if 0 in (x, y):
        a+=1
    else:
        if x>0:
            if y>0:
                q1+=1
            else:
                q4+=1
        else:
            if y>0:
                q2+=1
            else:
                q3+=1

print("Q1: {}".format(q1))
print("Q2: {}".format(q2))
print("Q3: {}".format(q3))
print("Q4: {}".format(q4))
print("AXIS: {}".format(a))