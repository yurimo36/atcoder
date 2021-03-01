# https://atcoder.jp/contests/arc056/tasks/arc056_a

a, b, k, l = map(int,input().split())

if a <= b/l:
    ans = a*k

else:
    ans = min(b*(k//l)+a*(k%l), b*(k//l+1))

print(ans)
