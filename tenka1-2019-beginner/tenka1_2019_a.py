# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_a

x, y ,z = map(int,input().split())

if min(x,y) < z < max(x,y):
    print("Yes")
else:
    print("No")