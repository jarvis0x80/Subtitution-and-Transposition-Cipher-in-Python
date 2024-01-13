# Input the cipher text from the transposition_enc.py and key used

cipherText = input("Enter cipher text: ")
transKey = input("Enter transposition key: ")
plaintextlist = []
cipherTextList = []

# Same symbols sets we used in transposition_enc.py
symbols1 = "$?@!%)&*"
symbols2 = "#(-=+></"
    
transKeyLength = len(transKey)
cipherTextLength = len(cipherText)
matrixWidth = cipherTextLength // transKeyLength
transKeySeq = []

# Convert the key to numrical format if it is not
for j in range(transKeyLength):
    seq = 1
    for k in transKey:
        if transKey[j] > k:
           seq = seq + 1 
    transKeySeq.append(str(seq))

# We'll creat matrix but invert the dimensions. 
si = 0
ei = matrixWidth
for s in range(transKeyLength):
    try:
        cipherTextList.append(cipherText[si:ei])
        si = ei
        ei = ei + matrixWidth  
    except IndexError:
        cipherTextList.append(cipherText[si:])

# Decrypt the cipher text
for i in range(matrixWidth):
    
    for j in range(1, transKeyLength + 1):
        charIndex = transKeySeq.index(str(j))
        plaintextlist.append(cipherTextList[charIndex][i])

plainText = "".join(plaintextlist)

# Replace the symbols from symbol set 1 to space
for c in plainText: 
    if c in symbols1:
        plainText = plainText.replace(c, ' ')

# Remove the symbols from symbol set 2       
for c in plainText:
    if c in symbols2:
        plainText = plainText.replace(c, '')

# We have our plain text back! (Wohooo)
print("Plaintext is: ", plainText)

