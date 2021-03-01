# https://atcoder.jp/contests/tenka1-2012-qualA/tasks/tenka1_2012_qualA_2

s = input().split()
ans = ""

for i in range(len(s)):
    ans += s[i]+ ","

print(ans[:-1])
