# https://atcoder.jp/contests/abc170/tasks/abc170_c

x, n = map(int,input().split())
li = list(map(int,input().split()))
ans = []

for i in range(n):
    ans.append(abs(li[i]-x))

ans.sort()
if 0 not in ans:
    print(x)
else:
    for i in range(1,1000):
        if ans.count(i) == 0:
            print(x-i)
            exit()
        elif ans.count(i) == 1:
            if x+i in li:
                print(x-i)
            else:
                print(x+i)
            exit()
