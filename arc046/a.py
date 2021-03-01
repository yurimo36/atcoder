# https://atcoder.jp/contests/arc046/tasks/arc046_a

n = int(input())
li = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ans = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

for i in range(2,7):
    x = [c*i for c in li]
    ans += x

print(ans[n-1])