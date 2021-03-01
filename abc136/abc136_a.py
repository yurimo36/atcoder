# https://atcoder.jp/contests/abc136/tasks/abc136_a

a, b, c = map(int,input().split())

ans = c - a + b

if ans < 0:
  ans = 0
  
print(ans)