# https://atcoder.jp/contests/abc047/tasks/arc063_a

s = list(input())
ans = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        ans += 1

print(ans)