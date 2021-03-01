# https://atcoder.jp/contests/abc091/tasks/abc091_b

n = int(input())
r = [input() for i in range(n)]
m = int(input())
b = [input() for i in range(m)]
rb = set(r+b)
ans = 0

for w in rb:
    x = r.count(w)
    y = b.count(w)
    if x-y > ans:
        ans = x-y

print(ans)