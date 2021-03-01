# https://atcoder.jp/contests/arc052/tasks/arc052_a

s = input()
ans = ""

for c in s:
    if c.isdecimal():
        ans += c

print(ans)