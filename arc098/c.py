# https://atcoder.jp/contests/arc098/tasks/arc098_a

n = int(input())
s = list(input())
w = []
e = []
x = 0
y = 0
ans = 1000000

#西と東の累積和を取る
for c in s:
    if c == "W":
        x += 1
    else:
        y += 1
    w.append(x)
    e.append(y)

for i in range(n):
    if i == 0:
        z = e[n-1] - e[i]
    elif i == n-1:
        z = w[i-1]
    else:
        z = w[i-1] + e[n-1] - e[i]
    if z < ans:
        ans = z

print(ans)