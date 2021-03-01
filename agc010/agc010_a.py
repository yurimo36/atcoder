# https://atcoder.jp/contests/agc010/tasks/agc010_a

n = int(input())
li = list(map(int,input().split()))
odd = 0
even = 0

for i in li:
  if i%2 == 0:
    even += 1
  else:
    odd += 1
    
if odd%2==0:
  print("YES")
else:
  print("NO")