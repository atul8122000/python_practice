# ######################### 2 program to check whether the string is Symmetrical or Palindrome #######################
S = 'malayalam'
# to reverse String
RS = S[::-1]
# to devide string in 2 part
half = int(len(S) / 2)

Fhalf = S[:half]
Lhalf = S[half:]

if S == RS and Fhalf == Lhalf:
    print("String is Palindrome and Symmetrical")
elif S == RS:
    print("string is Palindrome")
elif Fhalf == Lhalf:
    print("string is Symmetrical")
else:
    print("String is not Symmetrical or Palindrome")