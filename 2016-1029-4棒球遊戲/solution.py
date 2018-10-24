lines = [ input().split(" ") for line in range(9) ]
maxOutTime = int(input())
rounds = []
totalRoundAmount = 0

for idx, line in enumerate(lines):
  del lines[idx][0] # 把每一行最前面的數字拿掉
  totalRoundAmount += len(lines[idx])

rounds = [ k for i in list(map(list, zip(*lines))) for k in i ]

# for i in range(1, totalRoundAmount + 1):
#   if i > 9:
#     if i % 9 == 0:
#       x, y = (i - 1) // 9, 8
#     else:
#       x, y = i // 9, i % 9 - 1
#   elif i == 9:
#     x, y = 0, 8
#   else:
#     x, y = 0, i % 9 - 1

#   # print("i = {}, cord ({}, {})".format(i, x, y))

#   rounds.append(lines[y][x])

# print(rounds)

####

nowPlayer = [1, 0, 0, 0]
outCounter = 0
totalScore = 0

def score(playerList, N):
  newList = playerList[:] # deepcopy
  
  for idx, el in enumerate(playerList):
    if el == 0: continue

    if idx + N == 4:
      finalIdx = 0
    else:
      finalIdx = (idx + N) % 4
    
    # if finalIdx == 0:
    #   # 球員回到本壘，得分
    #   global totalScore
    #   totalScore += 1

    newList[finalIdx] = 1

  return newList

for idx, el in enumerate(rounds):
  if el == "1B":
    totalScore += nowPlayer[3]
    nowPlayer = score(nowPlayer, 1)
  elif el == "2B":
    totalScore += nowPlayer[3] + nowPlayer[2]
    nowPlayer = score(nowPlayer, 2)
  elif el == "3B":
    totalScore += nowPlayer[3] + nowPlayer[2] + nowPlayer[1]
    nowPlayer = score(nowPlayer, 3)
  elif el == "HR":
    totalScore += nowPlayer[3] + nowPlayer[2] + nowPlayer[1] + nowPlayer[0] + 1 # 全壘打，得分
    nowPlayer = score(nowPlayer, 4)
  elif el == "FO" or el == "GO" or el == "SO":
    outCounter += 1

    if outCounter == maxOutTime:
      break
    
    if outCounter % 3 == 0:
      nowPlayer = [1, 0, 0, 0] # reset

print(totalScore)

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
