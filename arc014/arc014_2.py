# https://atcoder.jp/contests/arc014/tasks/arc014_2

n = int(input())
li = [input() for i in range(n)]
x = li[0][0]
ans = []

for i in range(n):
    ans.append(li[i])
    if i == 0:
        y = li[i][-1]
    else:
        if ans.count(li[i]) == 1 and li[i][0] == y:
            y = li[i][-1]
        else:
            if i%2 == 1:
                print("WIN")
                exit()
            else:
                print("LOSE")
                exit()

print("DRAW")