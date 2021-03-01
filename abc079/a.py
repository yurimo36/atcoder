# https://atcoder.jp/contests/abc079/tasks/abc079_a

s = input()

for i in range(10):
    if s[1] == str(i) and s[2] == str(i):
        if s[0] == str(i) or s[3] == str(i):
            print("Yes")
            exit()

print("No")