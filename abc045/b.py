# https://atcoder.jp/contests/abc045/tasks/abc045_b

a = list(input())
b = list(input())
c = list(input())
x = "a"

while True:
    if x == "a":
        if len(a) == 0:
            print("A")
            exit()
        x = a.pop(0)
    if x == "b":
        if len(b) == 0:
            print("B")
            exit()
        x = b.pop(0)
    if x == "c":
        if len(c) == 0:
            print("C")
            exit()
        x = c.pop(0)