# https://atcoder.jp/contests/abc031/tasks/abc031_b

l, h = map(int,input().split())
n = int(input())
a = [int(input()) for i in range(n)]

for i in a:
    if i < l:
        print(l-i)
    elif i <= h:
        print(0)
    else:
        print(-1)