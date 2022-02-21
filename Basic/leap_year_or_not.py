year = int(input("Enter value for year"))

if (year%400 == 0) or (year%100 == 0) or (year%4 == 0):
    print ("year", year,"is an leap year")
else:
    print ("year", year,"is not leap year")