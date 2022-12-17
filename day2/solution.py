

def game(elfChoice, myChoice):
    points = 0
    if elfChoice == "A":
        #Mychoice Rock
        if myChoice == "X":
            #tie
            points += 3
        #Mychoice Paper
        elif myChoice == "Y":
            #win
            points += 6
        #Mychoice Scissors
        else:
            #lose
            points += 0
    
    #Elf Paper
    elif elfChoice == "B":
        #Mychoice Rock
        if myChoice == "X":
            #lose
            points += 0
        #Mychoice Paper
        elif myChoice == "Y":
            #tie
            points += 3
        #Mychoice Scissors
        else:
            #win
            points += 6
    #Elf Scissors
    else:
        #Mychoice Rock
        if myChoice == "X":
            #win
            points += 6
        #Mychoice Paper
        elif myChoice == "Y":
            #lose
            points += 0
        #Mychoice Scissors
        else:
            #tie
            points += 3
    
    return points

with open(f"day2\input.txt","r") as file:
    
    elfAction = []
    myAction = []
    for line in file:
        elfAction.append(line[0])
        myAction.append(line[2])


myPoints = 0
myPointsPT2 = 0

counter = 0
while counter < len(elfAction):
    elfChoice = elfAction[counter]
    myChoice = myAction[counter]
    #Points by choice
    #Rock
    if myChoice == "X":
        myPoints += 1
        
    #Paper
    elif myChoice == "Y":
        myPoints += 2
        
    #Scissors
    elif myChoice == "Z":
        myPoints += 3
        
    
    #Points by game A = Rock, B = Paper, C = Scissors
    #               X = Rock, Y = Paper, Z = Scissors

    #------------------Part One---------------------------

    myPoints += game(elfChoice, myChoice)
    
    #--------------------------Part two------------------------------

     #MYChoice 
     #X = Lose
     #Y = Tie
     #Z = Win

    if myChoice == "X":
        if elfChoice == "A": #Rock
            myPointsPT2 += game(elfChoice, "Z")
            myPointsPT2 += 3
        elif elfChoice == "B": #Paper
            myPointsPT2 += game(elfChoice, "X")
            myPointsPT2 += 1
        else: #Scissors
            myPointsPT2 += game(elfChoice, "Y")
            myPointsPT2 += 2
    elif myChoice == "Y":
        if elfChoice == "A": #Rock
            myPointsPT2 += game(elfChoice, "X")
            myPointsPT2 += 1
        elif elfChoice == "B": #Paper
            myPointsPT2 += game(elfChoice, "Y")
            myPointsPT2 += 2
        else: #Scissors
            myPointsPT2 += game(elfChoice, "Z")
            myPointsPT2 += 3
    else:
        if elfChoice == "A": #Rock
            myPointsPT2 += game(elfChoice, "Y")
            myPointsPT2 += 2
        elif elfChoice == "B": #Paper
            myPointsPT2 += game(elfChoice, "Z")
            myPointsPT2 += 3
        else: #Scissors
            myPointsPT2 += game(elfChoice, "X")
            myPointsPT2 += 1

        
    
    counter += 1

print(f"Total ponts: {myPoints}")

print(f"Total points (PT2): {myPointsPT2}")
            

