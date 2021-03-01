# https://atcoder.jp/contests/indeednow-qualb/tasks/indeednow_2015_qualb_2

s = input()
t = input()

if len(s) != len(t):
    print(-1)
    exit()

for i in range(len(s)):
    if s == t:
        print(i)
        exit()
    else:
        s = s[-1] + s[:-1]

print(-1)
