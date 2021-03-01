# https://atcoder.jp/contests/arc040/tasks/arc040_a

n = int(input())
li = [input() for i in range(n)]
r = 0
b = 0

for i in li:
    r += i.count("R")
    b += i.count("B")

if r > b:
    print("TAKAHASHI")
elif r < b:
    print("AOKI")
else:
    print("DRAW")