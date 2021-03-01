# https://atcoder.jp/contests/dp/tasks/dp_d

n, w = map(int,input().split())
weight = []
value = []
for i in range(n):
    x, y = map(int,input().split())
    weight.append(x)
    value.append(y)

dp = [[0]*(w+1) for i in range(n+1)]
# dp[i][sum_w] := i-1 番目までの品物から重さが sum_w を超えないように選んだときの、価値の総和の最大値
omosa = 0

for i in range(n):
    for omosa in range(w+1):
        if weight[i] <= omosa: #もし追加しても制限を超えないなら
            #i番目の商品を選ぶ場合
            dp[i+1][omosa] = max(dp[i+1][omosa], value[i] + dp[i][omosa-weight[i]])
        #i番目の商品を選ばない場合(これはいつでも起きる)
        dp[i+1][omosa] = max(dp[i+1][omosa], dp[i][omosa])

print(dp[n][w])