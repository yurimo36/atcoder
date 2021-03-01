# https://atcoder.jp/contests/abc025/tasks/abc025_b

n, a, b = map(int,input().split())
ans = 0

#westがプラス
for i in range(n):
    s = input().split()
    x = int(s[1])
    if s[0] == "East":
        if x < a:
            ans -= a
        elif x > b:
            ans -= b
        else:
            ans -= x
    else:
        if x < a:
            ans += a
        elif x > b:
            ans += b
        else:
            ans += x

if ans > 0:
    print("West " + str(abs(ans)))
elif ans < 0:
    print("East " + str(abs(ans)))
else:
    print(0)