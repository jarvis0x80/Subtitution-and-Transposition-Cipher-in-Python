# this is a program that will decrypt ciphertext 
# by subtitution & transposition method

cipherText = input("Enter cipher text: ")
subKey = int(input("Enter subtitution key: "))
transKey = input("Enter transposition key: ")

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

plainText = decrypt(cipherText)
print("Plaintext is: ", plainText)    