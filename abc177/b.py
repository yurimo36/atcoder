# https://atcoder.jp/contests/abc177/tasks/abc177_b

s = input()
t = input()
ans = 1000000

for i in range(len(s)-len(t)+1):
    x = 0
    for j in range(len(t)):
        if s[j+i] != t[j]:
            x += 1
    if x < ans:
        ans = x

print(ans)
