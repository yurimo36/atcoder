# https://atcoder.jp/contests/abc184/tasks/abc184_b

a, b = map(int, input().split())
s = list(input())

for c in s:
    if c == "o":
        b += 1
    else:
        b = max(b-1, 0)

print(b)
