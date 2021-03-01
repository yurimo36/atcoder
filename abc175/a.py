# https://atcoder.jp/contests/abc175/tasks/abc175_a

s = input()
ans = s.count('R')

if s == 'RSR':
    ans = 1

print(ans)
