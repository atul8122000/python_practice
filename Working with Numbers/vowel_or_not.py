#######################################
# vowel_or_not
#######################################
char = str(input("Enter Any value: "))
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print (char, "is vowel") 
elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
    print (char, "is vowel") 
else:
    print(char, "is constant")