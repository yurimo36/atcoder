# https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_b

n = int(input())
x = 0
ans = []

for i in range(1,10000000):
    x += i
    ans.append(i)
    if x >= n:
        break

if x != n:
    ans.remove(x-n)
  
for i in ans:
    print(i)