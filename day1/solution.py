#Solution to the Advent of code Day 1

contador = 1
elves = {}
with open("day1\list.txt","r") as file:
    
    comida = []
    for linea in file:
        
        if linea != "\n":
            comida.append(int(linea))
        
        else:
            elves[f"elve {contador}"] = comida
            contador += 1
            comida = []

if comida != []:
    elves[f"elve {contador}"] = comida

sumas = []

for i in elves.values():
    sumas.append(sum(i))

maxValue = None
maxIndex = None

for inx, num in enumerate(sumas):
    if(maxValue is None or num>maxValue):
        maxValue = num
        maxIndex = inx
keys = list(elves.keys())
print(f"The elve that carries more calories is {keys[maxIndex]} with {maxValue} calories")

sortedsumas = sorted(sumas)


print(f"total of the top three is {sortedsumas[-1]+ sortedsumas[-2] + sortedsumas[-3]}")