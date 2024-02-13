# This program wil encryp plaintext with subtitution and transposition method and decrypt ciphertext aswell.

plainText = input("Enter plain text: ")
subKey = int(input("Enter subtitution key: "))
transKey = input("Enter transposition key: ")

def encrypt(plainText):
    
    global subKey
    global transKey
    
    plainTextList = []
    cipherTextList = []
    upperAlphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerAlphabets = "abcdefghijklmnopqrstuvwxyz"
    symbols1 = "$?@!%)&*"
    symbols2 = "#(-=+></"
    
    transKeyLength = len(transKey)
    plainTextLength = len(plainText)
    matrixWidth = plainTextLength // transKeyLength
    remainder = plainTextLength % transKeyLength
    transKeySeq = []
    
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
            
    cipherText = "".join(cipherTextList)
    
    plainText = cipherText
    cipherTextList = []
    
    random = transKeyLength
    for c in plainText: 
        random = random + matrixWidth
        random = random % 7
        if c == ' ':
            plainText = plainText.replace(' ',symbols1[random])
            
    for j in range(transKeyLength):
        seq = 1
        for k in transKey:
            if transKey[j] > k:
              seq = seq + 1 
        transKeySeq.append(seq)
        
    si = 0
    ei = transKeyLength
    for s in range(matrixWidth):
        try:
            plainTextList.append(plainText[si:ei])
            si = ei
            ei = ei + transKeyLength  
        except IndexError:
            plainTextList.append(plainText[si:])
            
    random = transKeyLength
    if remainder > 0:
        lastRow = ""
        lastRow = lastRow + plainText[-remainder:]
        while len(lastRow) != transKeyLength:
            random = random + matrixWidth
            random = random % 7
            lastRow = lastRow + symbols2[random]
            
        plainTextList.append(lastRow)
        
    for col in transKeySeq:
        for row in plainTextList:
            cipherTextList.append(row[col-1])
            
    cipherText = "".join(cipherTextList)

    return cipherText

def decrypt(cipherText):
    
    upperAlphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerAlphabets = "abcdefghijklmnopqrstuvwxyz"
    symbols1 = "$?@!%)&*"
    symbols2 = "#(-=+></"
    plainTextList = []
    cipherTextList = []
    
  
    
    global subKey
    global transKey
    
    if subKey >= 26:
        subKey = subKey % 26
        
    transKeyLength = len(transKey)
    cipherTextLength = len(cipherText)
    matrixWidth = cipherTextLength // transKeyLength
    transKeySeq = [] 
    
    for j in range(transKeyLength):
        seq = 1
        for k in transKey:
            if transKey[j] > k:
                seq = seq + 1 
        transKeySeq.append(str(seq))
        
    si = 0
    ei = matrixWidth
    for s in range(transKeyLength):
        try:
            cipherTextList.append(cipherText[si:ei])
            si = ei
            ei = ei + matrixWidth  
        except IndexError:
            cipherTextList.append(cipherText[si:])
            
    for i in range(matrixWidth):
        
        for j in range(1, transKeyLength + 1):
            charIndex = transKeySeq.index(str(j))
            plainTextList.append(cipherTextList[charIndex][i])

    plainText = "".join(plainTextList)
    for c in plainText: 
        if c in symbols1:
            plainText = plainText.replace(c, ' ')
        
    for c in plainText:
        if c in symbols2:
            plainText = plainText.replace(c, '')
    
    cipherText = plainText
    plainTextList = []
    
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
    
    return plainText

cipherText = encrypt(plainText)
print("Cipher text is: ", cipherText)
choice = int(input("Do you want to decrypt this ciphertext? \n 1. Yes \n 2. No \nYour choice: "))

if choice == 1:
    plainText = decrypt(cipherText)
    print("Plaintext is: ", plainText)

print("\n----- Program ended. Thank you :) -----")  