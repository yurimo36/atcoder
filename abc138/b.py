# https://atcoder.jp/contests/abc138/tasks/abc138_b

n = int(input())
a = list(map(int,input().split()))
ans = 0.0

for i in a:
  ans = ans + 1/i
  
ans = 1/ans
print(ans)