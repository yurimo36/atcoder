# https://atcoder.jp/contests/abc029/tasks/abc029_b

ans = 0
for i in range(12):
    if input().count("r") > 0:
        ans += 1
print(ans)