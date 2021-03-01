# https://atcoder.jp/contests/arc003/tasks/arc003_1

n = int(input())
s = input()

print((s.count("A")*4 + s.count("B")*3 + s.count("C")*2 + s.count("D")) /n)