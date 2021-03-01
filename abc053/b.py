# https://atcoder.jp/contests/abc053/tasks/abc053_b

s = input()
x = 0
y = 0
ans = 1

for c in s:
    if c == "A":
        break
    x += 1
  
for c in s[::-1]:  
    if c == "Z":
        break
    y += 1

print(len(s)-x-y)