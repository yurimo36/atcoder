# https://atcoder.jp/contests/abc161/tasks/abc161_d

k = int(input())
lunlun = [1, 2, 3, 4, 5, 6, 7, 8, 9] #ルンルン数リスト

for i in range(k):
    x = lunlun[i]
    if x%10 != 0:
        lunlun.append(x*10+x%10-1)
    lunlun.append(x*10+x%10)
    if x%10 != 9:
        lunlun.append(x*10+x%10+1)
        #print(lunlun)
print(x)