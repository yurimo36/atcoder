# https://atcoder.jp/contests/abc048/tasks/abc048_b

x, y, z = map(int,input().split())
if x%z != 0:
    print(y//z - x//z)
else:
    print(y//z - x//z +1)