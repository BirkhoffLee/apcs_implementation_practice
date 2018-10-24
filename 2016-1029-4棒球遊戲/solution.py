lines = [ input().split(" ") for line in range(9) ]
maxOutTime = int(input())
rounds = []
totalRoundAmount = 0

for idx, line in enumerate(lines):
  del lines[idx][0] # 把每一行最前面的數字拿掉
  totalRoundAmount += len(lines[idx])

rounds = [ k for i in list(map(list, zip(*lines))) for k in i ]

nowPlayer = [1, 0, 0, 0]
outCounter = 0
totalScore = 0
m = 0

for idx, el in enumerate(rounds):
  if el == "1B":
    totalScore += nowPlayer[3]
    nowPlayer[3] = nowPlayer[2] 
    nowPlayer[2] = nowPlayer[1]
    nowPlayer[1] = 1
  elif el == "2B":
    totalScore += nowPlayer[3] + nowPlayer[2]
    nowPlayer[3] = nowPlayer[1] 
    nowPlayer[2] = 1
    nowPlayer[1] = 0
  elif el == "3B":
    totalScore += nowPlayer[3] + nowPlayer[2] + nowPlayer[1]
    nowPlayer[3] = 1
    nowPlayer[2] = 0
    nowPlayer[1] = 0
  elif el == "HR":
    totalScore += nowPlayer[3] + nowPlayer[2] + nowPlayer[1] + 1
    nowPlayer[3] = 0
    nowPlayer[2] = 0
    nowPlayer[1] = 0
  elif el == "FO" or el == "GO" or el == "SO":
    maxOutTime -= 1
    m += 1
    # outCounter += 1
    
    # if outCounter == maxOutTime:
    #   break

    # if outCounter % 3 == 0:
    #   nowPlayer[3] = nowPlayer[2] = nowPlayer[1] = 0
  if m == 3:
    nowPlayer[3] = nowPlayer[2] = nowPlayer[1] = 0
    m = 0
  if maxOutTime == 0: break


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
