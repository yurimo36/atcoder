# https://atcoder.jp/contests/abc066/tasks/arc077_a

n = int(input())
li = list(map(int,input().split()))

if n%2 == 0:
    ans = li[1::2][::-1] + li[::2]
else:
    ans = li[::2][::-1] + li[1::2]

print(*ans)