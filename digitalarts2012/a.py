# https://atcoder.jp/contests/digitalarts2012/tasks/digitalarts_1

li = input().split()
n = int(input())
t = [input() for i in range(n)]

for i in range(len(li)):
    for w in t:
        if li[i] == w:
            li[i] = "*"*len(w)
        elif "*" in w and len(w) == len(li[i]):
            y = 0
            for j in range(len(w)):
                if w[j] != "*" and w[j] != li[i][j]:
                    y = 1
                    break
            if y == 0:
                li[i] = "*"*len(w)

print(*li)
