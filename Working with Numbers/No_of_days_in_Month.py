#######################################
# No_of_days_in_Month
#######################################
month = int(input("Enter Month: "))
year =int(input("Enter Year: "))
if ((month == 2) and(year%400==0 or year%100==0 or year%4==0)):
    print("No of days is: 29")
elif month==2:
    print("No of days is:28")
elif (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print("No of days is:31")
else:
    print("No of days is:30")