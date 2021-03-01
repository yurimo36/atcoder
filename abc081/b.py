# https://atcoder.jp/contests/abc081/tasks/abc081_b

n = int(input())
li = list(map(int,input().split()))
ans = 1000000000000

for i in li:
  x = 0
  while i%2 == 0:
    i = i//2
    x += 1
  if x < ans:
    ans = x
    
print(ans)