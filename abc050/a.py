# https://atcoder.jp/contests/abc050/tasks/abc050_a

li = input().split()
x = int(li[0])
y = int(li[2])
print(x+y) if li[1]=="+" else print(x-y)