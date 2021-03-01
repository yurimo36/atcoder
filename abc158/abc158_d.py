# https://atcoder.jp/contests/abc158/tasks/abc158_d

ans = input()
q = int(input())
top = 0
first = str()
last = str()

for i in range(q):
    li =input().split()
    if li[0] =="1":
        top = (top+1)%2
    else:
        if li[1] == "1":
            if top ==0:
                first += li[2]
            else:
                last += li[2]
        else:
            if top ==1:
                first += li[2]
            else:
                last += li[2]

if top == 0:
    ans = first[::-1] + ans + last
else:
    ans = last[::-1] + ans[::-1] + first

print(ans)
