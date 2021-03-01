# https://atcoder.jp/contests/abc043/tasks/abc043_b

s = list(input())
ans = ""

for c in s:
  if c == "0":
    ans += "0"
  if c == "1":
    ans += "1"
  if c == "B":
    if ans != "":
      ans = ans[:len(ans)-1]

print(ans)