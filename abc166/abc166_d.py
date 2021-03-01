# https://atcoder.jp/contests/abc166/tasks/abc166_d

x = int(input())

def check(n):
    m = int(n**0.2)
    if abs(m**5 - n) < 1e-6:
        return True
    else:
        return False

for i in range(10**7):
    y = abs(x-i**5)
    if check(y):
        if x-i**5>0:
            print(i, int(y**0.2)*(-1))
        else:
            print(i, int(y**0.2))
        exit()