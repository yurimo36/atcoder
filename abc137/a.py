# https://atcoder.jp/contests/abc137/tasks/abc137_a

a, b = map(int,input().split())
x = [a+b, a-b, a*b]
print(max(x))