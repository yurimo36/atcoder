# https://atcoder.jp/contests/abc049/tasks/abc049_b

x, y = map(int,input().split())
ans = []

for i in range(x):
    s = input()
    ans.append(s)
    ans.append(s)

for i in ans:
    print(i)