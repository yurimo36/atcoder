# https://atcoder.jp/contests/zone2021/tasks/zone2021_a

s = list(input())
ans = 0

for i in range(9):
  x = s[i:i+4]
  if ''.join(x) == "ZONe":
    ans += 1

print(ans)
