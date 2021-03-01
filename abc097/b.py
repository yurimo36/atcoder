# https://atcoder.jp/contests/abc097/tasks/abc097_b

n = int(input())
li = []

for i in range(1,32):
    for j in range(2,11):
        x = i**j
        if x <= 1000:
            li.append(x)

li.sort()

for i in range(len(li)):
    if li[i] == n:
        print(n)
        exit()
    elif li[i] > n:
        print(li[i-1])
        exit()