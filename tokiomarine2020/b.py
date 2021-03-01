# https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_b

a, x = map(int,input().split())
b, y = map(int,input().split())
t = int(input())

if (x-y)*t >= abs(a-b):
    print("YES")
else:
    print("NO")
