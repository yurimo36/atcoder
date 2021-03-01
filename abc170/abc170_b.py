# https://atcoder.jp/contests/abc170/tasks/abc170_b

x, y = map(int,input().split())

for i in range(x+1):
    a = 2*i + 4*(x-i)
    if a == y:
        print("Yes")
        exit()

print("No")