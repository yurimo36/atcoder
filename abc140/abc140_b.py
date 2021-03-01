# https://atcoder.jp/contests/abc140/tasks/abc140_b

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
x = 0

ans = sum(b)

for i in range(0, n-1):
  if a[i] +1 == a[i+1]:
    x = a[i] - 1
    ans = ans + c[x]

print(ans)