# https://atcoder.jp/contests/code-formula-2014-quala/tasks/code_formula_2014_qualA_a

n = int(input())
li = [i**3 for i in range(1,101)]

if n in li:
    print("YES")
else:
    print("NO")