# https://atcoder.jp/contests/abc039/tasks/abc039_c

s = input()
s = s[:12]

if s == "WBWBWWBWBWBW":
    print("Do")
elif s == "WBWWBWBWBWWB":
    print("Re")
elif s == "WWBWBWBWWBWB":
    print("Mi")
elif s == "WBWBWBWWBWBW":
    print("Fa")
elif s == "WBWBWWBWBWWB":
    print("So")
elif s == "WBWWBWBWWBWB":
    print("La")
elif s == "WWBWBWWBWBWB":
    print("Si")