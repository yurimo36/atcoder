# https://atcoder.jp/contests/abc153/tasks/abc153_a

from sys import stdin

x,y = [int(x) for x in stdin.readline().rstrip().split()]
 
z = int(x/y)
if(x%y==0):
  print(z)
else:
  print(z+1)