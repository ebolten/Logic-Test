#setting user's imput of characters
characters = input('Enter characters: ')

#the size is set to the number of characters in variable
size = len(characters)

#a variable i is set to 0
i = 0

#while loop to check each character in variablle
while size > i:

    #setting a variable sequence to 0 and i to add 1 every time it loops
    sequence = 0
    i += 1

    #checks for characters xxx in characters
    if 'xxx' in characters[sequence:i]:
        print('A')
        sequence += 3
        characters = characters[i:size]

    #checks for characters xyx in characters
    elif 'xyx' in characters[sequence:i]:
        print('B')
        sequence += 3
        characters = characters[i:size]








