# https://atcoder.jp/contests/abc145/tasks/abc145_b

n = int(input())
s = input()

if n%2==1:
  print("No")
else:
  a = s[:int(n/2)]
  b = s[int(n/2):]
  if a==b:
    print("Yes")
  else:
    print("No")