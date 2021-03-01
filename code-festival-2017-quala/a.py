# https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_a

s = input()

if len(s) < 4:
    print("No")
    exit()

if s[:4] == "YAKI":
    print("Yes")
else:
    print("No")