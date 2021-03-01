# https://atcoder.jp/contests/abc132/tasks/abc132_c

n = int(input())
d = list(map(int,input().split()))
d.sort()

if d[int(len(d)/2)-1] == d[int(len(d)/2)]:
    print(0)
else:
    print(d[int(len(d)/2)]-d[int(len(d)/2)-1])