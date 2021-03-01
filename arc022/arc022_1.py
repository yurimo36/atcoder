# https://atcoder.jp/contests/arc022/tasks/arc022_1

s = input()
x = 0

for c in s:
    if (c == "i" or c == "I") and x == 0:
        x = 1
    if (c == "c" or c == "C") and x == 1:
        x = 2
    if (c == "t" or c == "T") and x == 2:
        print("YES")
        exit()

print("NO")