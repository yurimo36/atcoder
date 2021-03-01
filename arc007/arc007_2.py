# https://atcoder.jp/contests/arc007/tasks/arc007_2

n, m = map(int,input().split())
disk = [int(input()) for i in range(m)]
now = [i+1 for i in range(n)]
x = 0

for i in range(m):
    if x == disk[i]:
        continue
    y = now.index(disk[i])
    now[y] = x
    x = disk[i]

for i in now:
    print(i)