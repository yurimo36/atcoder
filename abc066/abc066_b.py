# https://atcoder.jp/contests/abc066/tasks/abc066_b

s = input()

for i in range(1,len(s)-1):
    s = s[:len(s)-1]
    if len(s)%2==1:
        continue
    else:
        if s[:len(s)//2] == s[len(s)//2:]:
            print(len(s))
            break