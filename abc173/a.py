# https://atcoder.jp/contests/abc173/tasks/abc173_a

n = int(input())
if n%1000 == 0:
    print(0)
else:
    print(1000-n%1000)