# https://atcoder.jp/contests/arc029/tasks/arc029_1

n = int(input())
li = [int(input()) for i in range(n)]
ans = []

for i in range(2 ** n):
    x = 0
    y = 0
    for j in range(n):
        if ((i >> j) & 1): #フラグが立っていたら
            x += li[j]
        else:
            y += li[j]
    ans.append(max(x,y))

print(min(ans))