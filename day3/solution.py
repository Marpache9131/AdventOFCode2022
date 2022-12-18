
def valueOfLetter(l):
    if l.isupper():
        return ord(l) - 38
    else:
        return ord(l) - 96

with open(f"day3\input.txt","r") as file:
    firstHalf = []
    secondHalf = []
    lines = []
    for line in file:
        lines.append(line[:len(line)-1])
        middleOfLine = int(len(line)/2)
        fh = line[:middleOfLine]
        sh = line[middleOfLine:len(line)-1]
        firstHalf.append(fh)
        secondHalf.append(sh)

items = []

counter = 0

for line in firstHalf:
    found = False
    for elementfh in line:
        secondHalfLine = secondHalf[counter]
        for elementsh in secondHalfLine:
            if elementfh == elementsh:
                items.append(elementfh)
                found = True
                break
        if found:
            counter += 1
            break

total = 0

for i in items:
    total += valueOfLetter(i)

print(total)

#-------------Part Two---------------
finalList = []
counter = 0
for counter in range(0,len(lines),3):
    firstLine = lines[counter]
    secondLine = lines[counter+1]
    thirdLine = lines[counter+2]
    found1 = False
    found2 = False
    for elementfl in firstLine:
        for elementsl in secondLine:
            if elementfl == elementsl:

                found1 = True
                break
        for elementtl in thirdLine:
            if elementfl == elementtl:
                
                found2 = True
                break
        if found1 and found2:
            finalList.append(elementfl)
            break
        else:
            found1 = False
            found2 = False
            
            

finalSum = 0
print(len(finalList))
for i in finalList:
    finalSum += valueOfLetter(i)

print(finalSum)
   