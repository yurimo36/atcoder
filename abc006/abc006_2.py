# https://atcoder.jp/contests/abc006/tasks/abc006_2

n = int(input())
x = 0
y = 0
z = 1

if n < 3:
    print(0)

elif n == 3:
    print(1)

else:
    for i in range(n-3):
        ans = (x + y + z)%10007
        x = y
        y = z
        z = ans
        
    print(ans%10007)