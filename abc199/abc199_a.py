# https://atcoder.jp/contests/abc199/tasks/abc199_a

a, b, c = map(int,input().split())

print("Yes") if a**2 + b**2 < c**2 else print("No")
