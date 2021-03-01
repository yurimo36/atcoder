# https://atcoder.jp/contests/code-formula-2014-quala/tasks/code_formula_2014_qualA_b

a, b = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
ans = ["x" for i in range(10)]

for i in p:
    i = (i-1)%10
    ans[i] = "."

for i in q:
    i = (i-1)%10
    ans[i] = "o"

print(*ans[6:])
print(" ", end="")
print(*ans[3:6])
print("  ", end="")
print(*ans[1:3])
print("   ", end="")
print(ans[0])
