# https://atcoder.jp/contests/abc136/tasks/abc136_c

n = int(input())
h = list(map(int,input().split()))

if n == 1:
    print("Yes")

else:
    x = h[0]
    for i in range(1,n):
        if h[i] <= x-2: #今までの最大値より2以上小さかったら
            print("No")
            break
        else:
            if i == n-1:
                print("Yes")
            if h[i] > x: #今までの最大値より大きかったら
                x = h[i] #最大値を更新