# https://atcoder.jp/contests/abc109/tasks/abc109_b

n = int(input())
w = [input() for i in range(n)]
x = 0

for i in range(n-1):
    if w.count(w[i]) == 1 and w[i][-1] == w[i+1][0]: #条件を満たしている
        continue
    else: #条件を満たしていない
        x = 1
        print("No")
        break

if x == 0:
    print("Yes")