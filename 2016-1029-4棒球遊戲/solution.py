lines = [ input().split(" ") for line in range(9) ]
maxOutTime = int(input())
rounds = []
totalRoundAmount = 0
k = 0

for idx, line in enumerate(lines):
  del lines[idx][0] # 把每一行最前面的數字拿掉
  totalRoundAmount += len(lines[idx])

for i in range(1, totalRoundAmount + 1):
  if i > 9:
    if i % 9 == 0:
      x, y = (i - 1) // 9, 8
    else:
      x, y = i // 9, i % 9 - 1
  elif i == 9:
    x, y = 0, 8
  else:
    x, y = 0, i % 9 - 1

  # print("i = {}, cord ({}, {})".format(i, x, y))

  rounds.append(lines[y][x])

print(rounds)

"""
    0  1  2  3  4
0   1B 1B FO GO 1B
1   1B 2B FO FO SO
2   SO HR SO 1B
3   FO FO FO HR
4   1B 1B 1B 1B
5   GO GO 3B GO
6   1B GO GO SO
7   SO GO 2B 2B
8   3B GO GO FO
"""

"""
1 9
2 10
3 11
4 12
5 13
6 14
7 15
8 16
"""