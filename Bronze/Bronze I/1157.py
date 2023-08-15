words = input().upper()
unique = list(set(words))

cnt = []
for w in unique:
    cnt.append(words.count(w))

if cnt.count(max(cnt)) >1 :
    print("?")
else:
    max_index = cnt.index(max(cnt))
    print(unique[max_index])