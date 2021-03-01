# https://atcoder.jp/contests/abc190/tasks/abc190_a

a, b, c = map(int, input().split())

if a + c > b:
    print('Takahashi')
else:
    print('Aoki')