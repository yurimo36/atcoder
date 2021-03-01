# https://atcoder.jp/contests/abc186/tasks/abc186_b

x, y = map(int,input().split())
li = []
ans = 0

for i in range(x):
    li += input().split()
m = int(min(li))

for i in li:
    ans += int(i)-m

print(ans)
