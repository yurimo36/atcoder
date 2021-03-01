# https://atcoder.jp/contests/abc106/tasks/abc106_c

s = input()
k = int(input())

for i in range(k):
    if s[i] != "1":
        print(s[i])
        exit()

print(1)