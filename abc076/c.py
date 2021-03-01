# https://atcoder.jp/contests/abc076/tasks/abc076_c

s = input()
t = input()
n = len(t)

for i in reversed(range(len(s)-n+1)): #後ろから一致する部分が無いか見ていく
    x = s[i:i+n]
    y = 0
    for j in range(n):
        if x[j] == "?" or x[j] == t[j]:
            continue
        else:
            y = 1
            break
    if y == 0:
        print(s[:i].replace("?", "a") +t + s[i+n:].replace("?", "a"))
        exit()

print("UNRESTORABLE")
