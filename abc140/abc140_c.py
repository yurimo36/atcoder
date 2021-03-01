# https://atcoder.jp/contests/abc140/tasks/abc140_c

n = int(input())
b = list(map(int,input().split()))
ans = 0

if n == 2:
    ans = b[0]*2

else:
    ans = b[0] + b[-1]

    for i in range(1, n-1):
        if b[i-1] < b[i]:
            ans = ans + b[i-1]
        else:
            ans = ans + b[i]

print(ans) 