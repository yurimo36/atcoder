# https://atcoder.jp/contests/abc116/tasks/abc116_b

s = int(input())
l = [s]
x = 1
y = 0

while y == 0:
  if s%2 == 0:
    s = int(s//2)
  else:
    s = 3*s+1

  if s in l:
    print(x+1)
    y = 1
  else:
    l.append(s)
    x += 1