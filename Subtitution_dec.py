# This is a program that will decrypt the ciphertext 
# by subtitution method

cipherText = input("Enter cipher text: ")
subKey = int(input("Enter subtitution key: "))
plainTextList = []

if subKey >= 26:
    subKey = subKey % 26

upperAlphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerAlphabets = "abcdefghijklmnopqrstuvwxyz"

for a in cipherText:
    
    if a in upperAlphabets:
        i = upperAlphabets.index(a)
        i = i - subKey
        plainTextList.append(upperAlphabets[i])
        continue
    elif a in lowerAlphabets:
        i = lowerAlphabets.index(a)
        i = i - subKey
        plainTextList.append(lowerAlphabets[i])
        continue
    else:
        plainTextList.append(a)

plainText = "".join(plainTextList)
print("Plaintext is: ", plainText)    