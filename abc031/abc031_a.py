# https://atcoder.jp/contests/abc031/tasks/abc031_a

x, y = map(int,input().split())
print(max(((x+1)*y, x*(y+1))))