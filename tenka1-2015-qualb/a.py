# https://atcoder.jp/contests/tenka1-2015-qualb/tasks/tenka1_2015_qualB_a

x = 100
y = 100
z = 200

for i in range(17):
    ans = x+y+z
    x = y
    y = z
    z = ans

print(ans)