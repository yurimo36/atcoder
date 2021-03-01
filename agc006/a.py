# https://atcoder.jp/contests/agc006/tasks/agc006_a

n = int(input())
s = input()
t = input()

for i in range(n):
    if s[i:] == t[:n-i]:
        print(n+i)
        exit()

print(2*n)
