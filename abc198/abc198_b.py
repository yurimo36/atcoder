# https://atcoder.jp/contests/abc198/tasks/abc198_b

s = input()

for i in range(10):
  n = len(s)
  x = s[:n//2]
  if n%2 == 0:
    y = s[n//2:]
  else:
    y = s[n//2+1:]
  if x[::-1] == y:
    print("Yes")
    exit()
  s = "0" + s

print("No")
