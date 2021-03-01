# https://atcoder.jp/contests/abc023/tasks/abc023_b

n = int(input())
s = input()
ans = "b"

n = int((n-1)/2)
for i in range(0,n+1):
    if i == 0:
        continue
    elif i%3 == 1:
        ans = "a" + ans + "c"
    elif i%3 == 2:
        ans = "c" + ans + "a"
    else:
        ans = "b" + ans + "b"

if s == ans:
    print(i)
else:
    print(-1)