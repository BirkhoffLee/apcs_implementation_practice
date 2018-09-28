amountOfPeople = input()
friendList = [ int(k) for k in input().split() ]
checkList = { k: False for k in friendList }
count = 0

for i, nextFriend in enumerate(friendList):
    # 檢查過的就跳過
    if checkList[i]:
        continue
    
    # 自己是自己的朋友
    if i == nextFriend:
        count += 1
        continue

    # linked list check
    nextPersonToCheck = nextFriend
    while not checkList[nextPersonToCheck]:
        # 如果檢查過了代表這個是圈圈開頭
        checkList[nextPersonToCheck] = True
        nextPersonToCheck = friendList[nextPersonToCheck]
    
    count += 1

print(count)