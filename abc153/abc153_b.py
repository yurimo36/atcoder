# https://atcoder.jp/contests/abc153/tasks/abc153_b

from sys import stdin

x,y = [int(x) for x in stdin.readline().rstrip().split()]
li = list(map(int,stdin.readline().rstrip().split()))

z = 0
for i in li:
    z = z + i

if(z<x):
    print("No")
else:
    print("Yes")