# https://atcoder.jp/contests/abc151/tasks/abc151_b

n, k, m = map(int,input().split())
a = list(map(int,input().split()))
sum = 0

for i in a:
    sum = sum + i

x = n * m - sum

if x > k:
    print("-1")
elif x < 0:
    print("0")
else:
    print(x)