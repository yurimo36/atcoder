# https://atcoder.jp/contests/abc113/tasks/abc113_c

n, m = map(int,input().split())
li = []
ans = []
#市, 年, 出力順で格納

for i in range(m):
    x = list(map(int,input().split()))
    x.append(i)
    li.append(x)

li.sort()

for i in range(len(li)):
    if i == 0:
        y = 1
    elif li[i][0] == li[i-1][0]:
        y += 1
    else:
        y = 1
    li[i].append(str(li[i][0]).rjust(6,'0') + str(y).rjust(6,'0'))

li.sort(key=lambda x: x[2])

for i in li:
    print(i[3])