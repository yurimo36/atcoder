# https://atcoder.jp/contests/agc024/tasks/agc024_a

a, b, c, k = map(int,input().split())

if k%2 == 1:
    ans = b-a

else:
    ans = a-b

print(ans)