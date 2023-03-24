while True:
    n = int(input())
    if n==0:
        break
    else:
        if len(str(n))%2==0: #짝수이면
            l=len(str(n))//2
            if str(n)[0:l]==str(n)[:l-1:-1]:
                print("yes")
            else:
                print("no")
        
        else: #홀수이면
            l=len(str(n))//2
            if str(n)[0:l]==str(n)[:l:-1]:
                print("yes")
            else:
                print("no")


'''더 좋은 답안
while True:
    n=input()
    if n=='0':
        break
    
    if n==n[::-1]:
        print("yes")
    else:
        print("no")

'''