# https://atcoder.jp/contests/abc040/tasks/abc040_b

n = int(input())
ans = 10000000

for i in range(1,1000):
    for j in range(i, 1000):
        x = n-i*j
        if x >= 0:
            y = j-i
            if x+y < ans:
                ans = x+y

print(ans)