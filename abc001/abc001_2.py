# https://atcoder.jp/contests/abc001/tasks/abc001_2

m = float(input())
m = m/1000
if m<0.1:
    print('00')
elif m<=5:
    m*=10
    if m<10:
        print('0'+str(int(m)))
    else:
        print(int(m))
elif m<=30:
    m+=50
    print(int(m))
elif m<=70:
    m=int((m-30)/5+80)
    print(m)
else:
    print('89')