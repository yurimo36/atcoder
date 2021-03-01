# https://atcoder.jp/contests/abc162/tasks/abc162_b

#全部の和 - 3の倍数の和 - 5の倍数の和 + 15の倍数の和

n = int(input())
ans = 0

for i in range(1,n+1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        ans += i

print(ans)