# https://atcoder.jp/contests/arc053/tasks/arc053_a

x, y = map(int,input().split())
ans = (x-1)*y + (y-1)*x
print(ans)