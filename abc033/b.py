# https://atcoder.jp/contests/abc033/tasks/abc033_b

n = int(input())
city = []
num = []

for i in range(n):
    x = input().split()
    city.append(x[0])
    num.append(int(x[1]))

if max(num) > sum(num)/2:
    print(city[num.index(max(num))])
else:
    print("atcoder")