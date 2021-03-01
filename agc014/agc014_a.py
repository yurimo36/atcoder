# https://atcoder.jp/contests/agc014/tasks/agc014_a

a, b, c = map(int,input().split())
ans = 0

if a == b == c and a%2 == 0:
    print(-1) #無限
    exit()

while a%2 == 0 and b%2 == 0 and c%2 == 0:
    ans += 1

    x = b//2 + c//2
    y = a//2 + c//2
    z = a//2 + b//2
    
    a = x
    b = y
    c = z

print(ans)
