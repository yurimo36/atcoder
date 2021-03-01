# https://atcoder.jp/contests/arc071/tasks/arc071_a

n = int(input())
li = [input() for i in range(n)]
ans = [51]*26 #a~z
s = ""

for word in li:
    for i in range(26):
        if word.count(chr(i+97)) < ans[i]:
            ans[i] = word.count(chr(i+97))

for i in range(26):
    s += chr(i+97)*ans[i]      

print(s)