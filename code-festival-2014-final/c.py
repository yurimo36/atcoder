# https://atcoder.jp/contests/code-festival-2014-final/tasks/code_festival_final_c


n = int(input())
li = []

for i in range(10,10001):
    i = str(i)
    x = len(i)
    y = 0
    for j in range(x):
        y += int(i[j])*(int(i)**(x-j-1))
    li.append(y)

if n in li:
    print(li.index(n)+10)
else:
    print(-1)