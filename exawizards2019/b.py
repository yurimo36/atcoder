# https://atcoder.jp/contests/exawizards2019/tasks/exawizards2019_b

n = int(input())
s = input()

if s.count("R") > s.count("B"):
    print("Yes")
else:
    print("No")