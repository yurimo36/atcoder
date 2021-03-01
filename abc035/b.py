# https://atcoder.jp/contests/abc035/tasks/abc035_b

s = list(input())
t = int(input())
s.sort(reverse=True)
x = 0
y = 0
z = s.count("?")

for i in range(len(s)-z):
    if s[i]=="L":
        x -= 1
    if s[i]=="R":
        x += 1
    if s[i]=="D":
        y -= 1
    if s[i]=="U":
        y += 1

ans = abs(x) + abs(y)

if t == 1:
    print(ans+z)
else:
    print(max(len(s)%2,ans-z))