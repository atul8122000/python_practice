#### Addition of two fraction

num1 = int(input("Enter First NO: "))
Deno1 = int(input("Enter denominators NO: "))
 
num2 = int(input("Enter Second NO: "))
Deno2 = int(input("Enter denominators NO: "))

if (Deno1 == Deno2):
    fraction = (num1 + num2)
    print(str(fraction)+ '/' + str(Deno1))
else:
    fraction = (num1 * Deno2) + (num2 * Deno1)
    print(str(fraction) + '/' + str(Deno1 * Deno2))