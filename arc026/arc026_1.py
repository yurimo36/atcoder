# https://atcoder.jp/contests/arc026/tasks/arc026_1

n, a, b = map(int,input().split())

if n <= 5:
    print(n*b)
else:
    print(b*5 + (n-5)*a)