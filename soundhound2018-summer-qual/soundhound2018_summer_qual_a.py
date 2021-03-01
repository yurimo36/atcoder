# https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_a

x, y = map(int,input().split())

if x*y == 15:
    print("*")
elif x+y == 15:
    print("+")
else:
    print("x")
