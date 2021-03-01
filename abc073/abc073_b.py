# https://atcoder.jp/contests/abc073/tasks/abc073_b

n = int(input())
ans = 0

for i in range(n):
  x, y = map(int,input().split())
  ans += y-x+1
  
print(ans)