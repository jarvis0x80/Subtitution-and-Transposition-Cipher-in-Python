# Import necessary librairies and get user input 

import random
plainText = input("Enter plain text: ")
transKey = input("Enter transposition key: ")
plainTextList = []
cipherTextList = []

# Two symbols set to replce space in Plain Text and Matrix 
# Caution: Dont input these symbols in Plain Text! if you want to use these in input, replace these symbols set with something else that you dont input as Plain Text

symbols1 = "$?@!%)&*"
symbols2 = "#(-=+></"
    
transKeyLength = len(transKey)
plainTextLength = len(plainText)
matrixWidth = plainTextLength // transKeyLength
remainder = plainTextLength % transKeyLength
transKeySeq = []

# Replace spaces in Plain Text with symbol from symbol set 1
spaceReplacedPlainText = ""
for char in plainText:
    if char == " ":  # Check if the character is a space
        spaceReplacedPlainText += random.choice(symbols1)  # Replace space with a random symbol
    else:
        spaceReplacedPlainText += char  # Keep the character unchanged if it's not a space

plainText = spaceReplacedPlainText
    
# Make an int Transposition Key, if the input is text then convert to int
for j in range(transKeyLength):
    seq = 1
    for k in transKey:
        if transKey[j] > k:
           seq = seq + 1 
    transKeySeq.append(seq)

# Make a 2d list matrix of the Plain Text
si = 0
ei = transKeyLength
for s in range(matrixWidth):
    try:
        plainTextList.append(plainText[si:ei])
        si = ei
        ei = ei + transKeyLength  
    except IndexError:
        plainTextList.append(plainText[si:])

# Fill the spaces in the last row of matrix with symbols set 2
if remainder > 0:
    lastRow = ""
    lastRow = lastRow + plainText[-remainder:]
    while len(lastRow) != transKeyLength:

        lastRow = lastRow + symbols2[random.randint(0,6)]
        
    plainTextList.append(lastRow)
   
 
for col in transKeySeq:
    for row in plainTextList:
        cipherTextList.append(row[col-1])
                
cipherText = "".join(cipherTextList)
print("Ciphertext is: ", cipherText)
