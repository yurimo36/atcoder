# https://atcoder.jp/contests/abc187/tasks/abc187_a

li = input().split()
i = 0
x = 0
y = 0

for i in range(3):
    x += int(li[0][i])
    y += int(li[1][i])

print(max(x,y))
