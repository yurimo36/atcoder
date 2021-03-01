# https://atcoder.jp/contests/abc186/tasks/abc186_c

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

n = int(input())
ans = 0

for i in range(1, n+1):
    if "7" not in str(i) and "7" not in Base_10_to_n(i, 8):
        ans += 1

print(ans)
