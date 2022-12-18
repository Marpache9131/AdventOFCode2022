import re

def isInList(list1,list2):
    verif = 0
    for elementL1 in list1:
        if elementL1 in list2:
            verif += 1
        else:
            break
    if verif == len(list1):
        return True
    else:
        return False

def isInList2(list1,list2):
    verif = 0
    for elementL2 in list2:
        if elementL2 in list1:
            verif += 1
            break
        else:
            break
    if verif != 0:
        return True
    else:
        return False
        

with open(f"day4\input.txt","r") as file:
    pairs = []
    for line in file:
        if "\n" in line:
            line = line[:len(line)-1]
        
        line = re.split(r'[,-]', line)
        p = []
        for i in range(int(line[0]),int(line[1])+1):
            p.append(i)
        pairs.append(p)
        p = []
        for i in range(int(line[2]),int(line[3])+1):
            p.append(i)
        pairs.append(p)

count = 0
for counter in range(0,len(pairs),2):
    firstPair = pairs[counter]
    secondPair = pairs[counter+1]

    if isInList(firstPair, secondPair):
        count += 1
    elif isInList(secondPair, firstPair):
        count += 1

print(count)


count = 0
for counter in range(0,len(pairs),2):
    firstPair = pairs[counter]
    secondPair = pairs[counter+1]
    firstPair = set(firstPair)
    secondPair = set(secondPair)

    
    if firstPair.intersection(secondPair):
        count += 1
    elif secondPair.intersection(firstPair):
        count += 1

print(count)
