# https://atcoder.jp/contests/abc182/tasks/abc182_c

li = [int(i) for i in list(input())]
ans = 0
x = 0

for i in li:
    x += i
y = x%3

if y != 0:
    if len(li) == 1:
        ans = -1
    else:
        for i in li:
            if i%3 == y:
                ans = 1
                break
        if ans != 1:
            if len(li) == 2:
                ans = -1
            else:
                ans = 2

print(ans)
