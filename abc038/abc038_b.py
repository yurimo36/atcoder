# https://atcoder.jp/contests/abc038/tasks/abc038_b

a, b = map(int,input().split())
c, d = map(int,input().split())

if c == a or c == b or d == a or d == b:
    print("YES")
else:
    print("NO")