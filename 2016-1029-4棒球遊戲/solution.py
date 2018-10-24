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
    outCounter += 1
    
    if outCounter == maxOutTime:
      break

    if outCounter % 3 == 0:
      nowPlayer[3] = nowPlayer[2] = nowPlayer[1] = 0

print(totalScore)
