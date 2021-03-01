# https://atcoder.jp/contests/abc062/tasks/abc062_b

x, y = map(int,input().split())
ans = [["#"]*(y+2)]
s = []

for i in range(x):
    s = "#" + input() + "#"
    ans.append(list(s))

ans.append(["#"]*(y+2))

for a in ans:
    for b in a:
        print(b, end ="")
    print()