# https://atcoder.jp/contests/code-festival-2017-qualc/tasks/code_festival_2017_qualc_a

s = input()

for i in range(len(s)-1):
    if s[i] == "A" and s[i+1] == "C":
        print("Yes")
        exit()
print("No")