# https://atcoder.jp/contests/discovery2016-qual/tasks/discovery_2016_qual_a

n = int(input())
s = "DiscoPresentsDiscoveryChannelProgrammingContest2016"
m = len(s)

for i in range((m+n-1)//n):
    print(s[n*i:n*(i+1)])