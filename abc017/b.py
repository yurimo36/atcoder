# https://atcoder.jp/contests/abc017/tasks/abc017_2

li = list(input())
l = len(li)
x = 0

for i in range(l):
    c = li[i]
    if x == 1:
        x = 0
        continue
    elif c != "c" and c != "o" and c != "k" and c != "u":
        print("NO")
        exit()
    elif c == "c" and i == l-1:
        print("NO")
        exit()
    elif c == "c" and li[i+1] != "h":
        print("NO")
        exit()
    if c == "c" and li[i+1] == "h":
        x = 1

print("YES")