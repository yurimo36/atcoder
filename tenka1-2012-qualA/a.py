# https://atcoder.jp/contests/tenka1-2012-qualA/tasks/tenka1_2012_qualA_1

n = int(input())
li = [1, 1]

for i in range(n-1):
    li.append(li[i]+li[i+1])

print(li[-1])