# 輸入：
# 第一行 迷宮行數 N
# 第二行 第一步走訪方向：0 左、1 上、2 右、3 下
# 3~N 行：迷宮

debug = False

# N = int(input()) if not debug else 3
# initialDirection = int(input()) if not debug else 1
N = int(input()) if not debug else 5
initialDirection = int(input()) if not debug else 0
idxOfMazeCenter = int((N - 1) / 2)
mazeList = []
mazeSeq = ""

if debug:
    # mazeList = [['4', '1', '2'], ['3', '0', '5'], ['6', '7', '8']]
    mazeList = [[3, 4, 2, 1, 4], [4, 2, 3, 8, 9], [2, 1, 9, 5, 6], [4, 2, 3, 7, 8], [1, 2, 6, 4, 3]]
else:
    for i in range(N):
        numbers = [ int(k) for k in input().split() ]
        mazeList.append(numbers)

def moveCursor(x, y, direction, steps):
    new_x, new_y = 0, 0
    numbers = []

    if direction == 0:
        # left
        new_x = x - steps
        new_y = y
        for i in range(steps):
            numbers.append(mazeList[y][x - (i + 1)])
    elif direction == 1:
        # up
        new_x = x
        new_y = y - steps
        for i in range(steps):
            numbers.append(mazeList[y - (i + 1)][x])
    elif direction == 2:
        # right
        new_x = x + steps
        new_y = y
        for i in range(steps):
            numbers.append(mazeList[y][x + (i + 1)])
    elif direction == 3:
        # down
        new_x = x
        new_y = y + steps
        for i in range(steps):
            numbers.append(mazeList[y + (i + 1)][x])

    return new_x, new_y, numbers

x, y = (idxOfMazeCenter, idxOfMazeCenter)
result = [mazeList[x][y]]
lastStep = 0
dirMap = {0: [0, 1, 2, 3], 1: [1, 2, 3, 0], 2: [2, 3, 0, 1], 3: [3, 0, 1, 2]}

for i in range(2 * N - 1):
    if i > 3:
        k = i % 4
    else:
        k = i

    direction = dirMap[initialDirection][k]

    if direction > 3:
        direction -= 3

    if i == 0:
        step = 1
    elif i % 2 == 0:
        step = i / 2 + 1
    else:
        step  = (i + 1) / 2
    
    if 2 * N - 2 == i:
        # it's the last route, step is same as previous one
        step = lastStep

    lastStep = step

    step = int(step)

    x, y, numbers = moveCursor(x, y, direction, step)
    for j in numbers:
        result.append(j)

result = [ str(k) for k in result ]

print("".join(result))
