# https://atcoder.jp/contests/arc057/tasks/arc057_a

x, y = map(int,input().split())
ans = 0

if y == 0:
    print(2*(10**12)-x)
    exit()

while x < 2*(10**12):
    x += 1 + x*y
    ans += 1
    #print(ans,x)

print(ans)