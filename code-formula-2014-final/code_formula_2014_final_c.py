# https://atcoder.jp/contests/code-formula-2014-final/tasks/code_formula_2014_final_c

li = input().split()
ans = []

for w in li:
    if "@" in w:
        l = w.split("@")
        for i in l[1:]:
            if i != "":
                ans.append(i)

ans = list(set(ans))
ans.sort()

if ans == []:
    print()
    exit()
for w in ans:
    print(w)
