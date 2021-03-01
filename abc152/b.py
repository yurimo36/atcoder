# https://atcoder.jp/contests/abc152/tasks/abc152_b

a, b = map(int,input().split())

if a <= b:
    print(str(a)*b)
else:
    print(str(b)*a)