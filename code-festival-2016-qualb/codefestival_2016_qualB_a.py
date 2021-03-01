# https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_a

s = input()
t = "CODEFESTIVAL2016"
ans = 0

for i in range(16):
    if s[i] != t[i]:
        ans += 1

print(ans)