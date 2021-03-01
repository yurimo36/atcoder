# https://atcoder.jp/contests/abc114/tasks/abc114_b

s = input()
ans = 1000

for i in range(len(s)-2):
    x = int(s[i:i+3])
    if abs(753-x) < ans:
        ans = abs(753-x)

print(ans)