# https://atcoder.jp/contests/abc200/tasks/abc200_b

n, k = map(int,input().split())

for i in range(k):
  if n % 200 == 0:
    n = n // 200
  else:
    n = int(str(n)+"200")

print(n)
