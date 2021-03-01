# https://atcoder.jp/contests/abc101/tasks/arc099_a

x, y = map(int,input().split())
li = list(map(int,input().split()))

if (x-1)%(y-1) == 0:
    print((x-1)//(y-1))
else:
    print((x-1)//(y-1)+1)