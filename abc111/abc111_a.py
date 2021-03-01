# https://atcoder.jp/contests/abc111/tasks/abc111_a

s=list(input())
for c in s:
  if c == "1":
    print("9",end="")
  elif c == "9":
    print("1",end="")
  else:
    print(c)
print()