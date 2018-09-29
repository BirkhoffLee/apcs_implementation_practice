args = [ int(k) for k in input().split() ]
N = args[0]
M = args[1]

numbers = []
maxNums = []
canDivideNums = []

for i in range(N):
    thisLineNum = [ int(k) for k in input().split() ]
    numbers.append(thisLineNum)
    maxNums.append(max(thisLineNum))

S = sum(maxNums)

print(S)

for j in maxNums:
    if S % j == 0:
        canDivideNums.append(str(j))

if len(canDivideNums) == 0: canDivideNums = ["-1"]

print(" ".join(canDivideNums))