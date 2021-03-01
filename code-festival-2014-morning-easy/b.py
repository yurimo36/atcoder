# https://atcoder.jp/contests/code-festival-2014-morning-easy/tasks/code_festival_morning_easy_b

n = int(input())
li = [i for i in range(1,21)]
ans = []

for i in range(10):
    if i%2 == 0:
        ans += li
    else:
        ans += reversed(li)

print(ans[n-1])