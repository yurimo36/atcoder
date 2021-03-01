# https://atcoder.jp/contests/abc029/tasks/abc029_c

n = int(input())
ans = ["a", "b", "c"]

for i in range(2,n+1):
    x = ["a"+c for c in ans]
    y = ["b"+c for c in ans]
    z = ["c"+c for c in ans]
    ans = x+y+z

for c in ans:
    print(c)
