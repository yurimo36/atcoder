# https://atcoder.jp/contests/dwacon6th-prelims/tasks/dwacon6th_prelims_a

n = int(input())
s = []
t = []
for i in range(n):
    li = input().split()
    s.append(li[0])
    t.append(int(li[1]))
x = input()

i = s.index(x)
print(sum(t[i+1:]))