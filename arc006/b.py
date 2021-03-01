# https://atcoder.jp/contests/arc006/tasks/arc006_2

n, m = map(int,input().split())
li = [list(input()) for i in range(m+1)]

x = li.pop(-1) #最後の行
ans = (x.index("o"))

if n == 1: #線が一本の場合
    print(1)
    exit()

for l in reversed(li): #下から見ていく
    if ans == 0:
        if l[ans+1] == "-":
            ans += 2

    elif ans == (n-1)*2:
        if l[ans-1] == "-":
            ans -= 2
    else:
        if l[ans+1] == "-":
            ans += 2
        elif l[ans-1] == "-":
            ans -= 2

print(ans//2+1)