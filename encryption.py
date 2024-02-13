# this is a program that will encrypt plaintext 
# by subtitution & transposition method

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
    
cipherText = encrypt(plainText)
print("Cipher text is: ", cipherText)
    
    
    