
row = [[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',]
       ,[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',]
       ,[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',]
       ,[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',]
       ,[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',]
       ,[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',]
       ,[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',]
       ,[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',]
        ,[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',]]

b = 10
blackChar = f' {chr(9675)} ' # Characters used
whiteChar = f' {chr(9679)} '
userInput = 0 # Initialized to 0
breakLoop = False
evenOdd = 0

# row[0][0] = ' o ' or ' O '

# Initial Board

print("You do not have to have a space between points.\nEx: 12, 31, 45, etc")
print("________________________________________")
for i in range(len(row)): # Prints the board out from row variable
    b -= 1
    print(f"{b} |{' '.join(row[i])}|")
print('    1   2   3   4   5   6   7   8   9')


while userInput != 'stop':
    if evenOdd%2 == 0: # If Even, black Goes
        userInput = input("Black moves - Select X and Y Values: ")
    
        if userInput == 'stop' or userInput == 'Stop' or userInput == 'STOP': # Stops program if user inputs stop
            breakLoop = True
            break
        userList = list(userInput)

        if len(userList) > 2 or len(userList) < 2: # Checks if the user input is in range
            print('Your input was invalid.')
            continue # Iterates the loop again

        splitValues = []
        for k in userList:
            splitValues.append(int(k))

        if 0 in splitValues: # Checks if there is a zero in the input -> If there is it will just reiterate the loop
            print('Your input was invalid.')
            continue

        xValue = splitValues[0]-1 # Finds the number that would insert the stone in the proper list
        yValue = 9-splitValues[1]

        if row[yValue][xValue] == ' . ': # Checks if ' - ' is the current value in the list, if it is it will replace it
            row[yValue][xValue] = blackChar

        else: # If there isn't a ' - ' then there is a stone so we must iterate through the loop again
            print('There was already a stone placed there.')
            continue

        counter = 10 
        print("________________________________________")
        for j in range(len(row)):
            counter -= 1
            print(f"{counter} |{' '.join(row[j])}|")
        print('    1   2   3   4   5   6   7   8   9')

    else: # if Odd, white goes
        userInput = input("White moves - Select X and Y Values: ")

        if userInput == 'stop' or userInput == 'Stop' or userInput == 'STOP':
            breakLoop = True
            break
        userList = list(userInput)

        if len(userList) > 2 or len(userList) < 2:
            print('Your input was invalid.')
            continue
        splitValues = []
        for k in userInput:
            splitValues.append(int(k))
        if 0 in splitValues:
            print('Your input was invalid.')
            continue
        xValue = splitValues[0]-1 
        yValue = 9-splitValues[1]
        if row[yValue][xValue] == ' . ':
            row[yValue][xValue] = whiteChar
        else:
            print('There was already a stone placed there.')
            continue



        counter = 10
        print("________________________________________")
        for j in range(len(row)):
            counter -= 1
            print(f"{counter} |{' '.join(row[j])}|")
        print('    1   2   3   4   5   6   7   8   9')
    evenOdd += 1
    
    if breakLoop:
        break
