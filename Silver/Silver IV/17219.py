n, m = map(int, input().split())
password = {}
for _ in range(n):
    add, pas = input().split()
    password[add]=pas

for _ in range(m):
    find = input()
    print(password.get(find))

    