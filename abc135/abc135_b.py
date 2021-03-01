# https://atcoder.jp/contests/abc135/tasks/abc135_b

n = int(input())
p = list(map(int,input().split()))
q = list(range(1, n+1)) #正しい昇順リスト
c = 0

if p == q:
  print("YES")

else:
  for i in range(n): #違う箇所の数を探す
    if p[i] != q[i]: #違ったら
      c = c + 1 #cを+1
    if c > 2: #違う箇所が2を超えたら見込みがないので抜ける
      break
  if c == 2: #2なら入れ替え1回で直る
    print("YES")
  else: #それ以外なら無理
    print("NO")