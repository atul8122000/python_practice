#######################################
# Alphabet_or_not
#######################################
char = str(input("Enter Any value: "))
cha= ord(char)
if 65<=cha<=90:
    print(char, "is capital alphabets")
elif 97<=cha<=122:
    print(char,"is Small alphabets")   
elif 48<=cha<=57:
    print("Digits") 
else:
    print(char,"is Special character")