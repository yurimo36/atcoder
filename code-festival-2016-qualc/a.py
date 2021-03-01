# https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_a

s = list(input())
x = 0

for c in s:
    if c == "C":
        x = 1
    elif c == "F" and x == 1:
        print("Yes")
        exit()

print("No")