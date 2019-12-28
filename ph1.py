#Vigenere cipher in python 3.6.3
#17007981    Christopher Martin
#The inputs for this code will be imported from the file in the portfolio folder called inputs.py
import inputs
#we will need a base alphabet to refer to in later parts of the code
baseAlphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
#fixed values will be used for testing purposes, but in the final version raw inputs will be used to make both the key and the plaintext easily changed
plainText= inputs.Text()
plainList= list(plainText)
#print("plainList", plainList)
key=  inputs.Key()
#adding the basic key to the cipher list
cipherList=list(key)
#appended the key list to add in all missing letters after the completed key in a list.
while (len(cipherList)<len(baseAlphabet)):
  for chr in baseAlphabet:
    if(chr not in cipherList):
      cipherList.append(chr)
#print ("cipherList", cipherList)
#This is where the completed cipher text will be appended to

cipherText=[]
baseIndexList=[]
for chr in plainText:
    baseIndex=baseAlphabet.index(chr)
    #print baseIndex
    baseIndexList.append(baseIndex)
#print baseIndexList

# next we use the indexed list of the locations of the letters in plaintext to reference the cipher list to get the final message
index = 0
for chr in plainText:
  cipherText.append(cipherList[baseIndexList[index]])
  index += 1
cipherText=''.join(cipherText)
print(cipherText)
