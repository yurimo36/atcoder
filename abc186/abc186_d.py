# https://atcoder.jp/contests/abc186/tasks/abc186_d

n = int(input())
li = list(map(int,input().split()))
li.sort(reverse=True)
ans = 0

for i in range(n):
  ans += li[i]*(n-1-2*i)

print(ans)
