# https://atcoder.jp/contests/abc189/tasks/abc189_a

s = list(input())

if s[0] == s[1] and s[1] == s[2]:
    print("Won")
else:
    print("Lost")