# https://atcoder.jp/contests/abc032/tasks/abc032_b

s = input()
n = int(input())
li = []

for i in range(len(s)-n+1):
    li.append(s[i:i+n])

print(len(set(li)))