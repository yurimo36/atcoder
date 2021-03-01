# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b

s = input()
n = len(s)
w = "keyence"
 
for i in range(7):
    if s[:i] == w[:i] and s[n-7+i:] == w[i:]:
        print("YES")
        exit()

print("NO")