# https://atcoder.jp/contests/code-formula-2014-qualb/tasks/code_formula_2014_qualB_b

n = list(input())
x = 0
y = 0
n = n[::-1]

for i in range(len(n)):
    if i%2 == 0:
        y += int(n[i])
    else:
        x += int(n[i])

print(x, y)