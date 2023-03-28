import sys

n = int(sys.stdin.readline())
word_list = []

for i in range(n):
    word_list.append(sys.stdin.readline().strip()) #이렇게 하면 input보다 빠름

#set()은 중복을 없을 수 있다.
word = set(word_list)
word_list = list(word)
word_list.sort() #사전순
word_list.sort(key=len) #길이순

for i in range(len(word_list)):
    print(word_list[i])
