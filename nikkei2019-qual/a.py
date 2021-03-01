# https://atcoder.jp/contests/nikkei2019-qual/tasks/nikkei2019_qual_a

x, y, z = map(int,input().split())
print(min(y,z), max(0,y+z-x))