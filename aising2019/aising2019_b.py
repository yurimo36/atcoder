# https://atcoder.jp/contests/aising2019/tasks/aising2019_b

n = int(input())
a, b = map(int,input().split())
li = list(map(int,input().split()))
x = 0
y = 0
z = 0

for i in li:
    if i <= a:
        x += 1
    elif i <= b:
        y += 1
    else:
        z += 1

print(min(x,y,z))