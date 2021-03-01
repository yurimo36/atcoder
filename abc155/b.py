# https://atcoder.jp/contests/abc155/tasks/abc155_b

n = int(input())
a = list(map(int,input().split()))
x = 0

for i in a:
  if i%2==1:
    continue
  elif i%3==0:
    continue
  elif i%5==0:
    continue
  else:
    print("DENIED")
    x = 1
    break
    
if x == 0:
  print("APPROVED")