# https://atcoder.jp/contests/arc037/tasks/arc037_a

n = int(input())
li = list(map(int,input().split()))
ans = 0

for i in li:
    if i < 80:
        ans += 80-i

print(ans)