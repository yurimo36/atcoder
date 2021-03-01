# https://atcoder.jp/contests/abc063/tasks/arc075_a

n = int(input())
s = [int(input()) for i in range(n)]
s.sort()
x = 0
y = 0

if sum(s)%10 != 0:
    print(sum(s))

else:
    while y == 0:
        if s[x]%10 != 0:
            s.pop(x)
            y = 1
            break
        else:
            x += 1
        
        if x >= len(s)-1:
            print(0)
            exit()

    print(sum(s))