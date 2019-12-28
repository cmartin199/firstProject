#Vigenere cipherText decoder (will decode any vigenere cipherText text provided you can enter the key) in python 3.6.3
#17007981    Christopher Martin


#we will need a base alphabet to refer to in later parts of the code
baseAlphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
cipherText= input("please enter the text to be decodes")
plainList= list(cipherText)
#print("plainList", plainList)
key=  input("please enter the key for the text to be decoded")
#adding the basic key to the cipherText list
cipherTextList=list(key)
#appended the key list to add in all missing letters after the completed key in a list.
while (len(cipherTextList)<len(baseAlphabet)):
  for chr in baseAlphabet:
    if(chr not in cipherTextList):
      cipherTextList.append(chr)
#print ("cipherTextList", cipherTextList)
#This is where the completed cipherText text will be appended to

plainText=[]
baseIndexList=[]
for chr in cipherText:
    baseIndex=cipherTextList.index(chr)
    #print baseIndex
    baseIndexList.append(baseIndex)
#print baseIndexList

# next we use the indexed list of the locations of the letters in cipherText to reference the cipherText list to get the final message
index = 0
for chr in cipherText:
  plainText.append(baseAlphabet[baseIndexList[index]])
  index += 1
plainText=''.join(plainText)
print(plainText)
