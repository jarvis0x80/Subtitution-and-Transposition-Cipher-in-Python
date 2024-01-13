# This is a program that will encrypt plain text 
# by subtitution method
 
# Get user input 
plainText = input("Enter plain text: ")
subKey = int(input("Enter subtitution key(integer): "))

cipherTextList = [] 

# Take mod of the key if it is bigger than 26
if subKey >= 26:
    subKey = subKey % 26

upperAlphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerAlphabets = "abcdefghijklmnopqrstuvwxyz"

'''
Following for loop will only encrypt the upper and lower Alphabets 
characters. Numbers and symbols in plainText will be escaped and produced
same in the cipherText
'''
for a in plainText:
    
    if a in upperAlphabets:
        i = upperAlphabets.index(a)
        i = i + subKey
        if i > 25:
            i = i % 26
        cipherTextList.append(upperAlphabets[i])
        continue
    elif a in lowerAlphabets:
        i = lowerAlphabets.index(a)
        i = i + subKey
        if i > 25:
            i = i % 26
        cipherTextList.append(lowerAlphabets[i])
        continue
    else:
        cipherTextList.append(a)

# Join the characters in list and to produce string and output cipherText 
cipherText = "".join(cipherTextList)
print("Ciphertext is: ", cipherText)  