# https://atcoder.jp/contests/arc047/tasks/arc047_a

a, b = map(int,input().split())
s = input()
now = 1
ans = 0

for c in s:
    if c == "+":
        now += 1
    else:
        now -= 1
    
    if now > b:
        now = 1
        ans += 1

print(ans)