# https://atcoder.jp/contests/abc067/tasks/arc078_a

n = int(input())
li = list(map(int,input().split()))
ans = 10000000000000
x = 0
y = sum(li)

for i in range(0,n-1):
    x += li[i]
    y -= li[i]
    z = abs(x-y)
    if z < ans:
        ans = z

print(ans)