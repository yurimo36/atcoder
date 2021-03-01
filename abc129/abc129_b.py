# https://atcoder.jp/contests/abc129/tasks/abc129_b

n = int(input())
w = list(map(int,input().split()))
ans = 10000000000

for i in range(1,n):
  x = abs(sum(w[:i]) - sum(w[i:]))
  if x < ans:
    ans = x

print(ans)