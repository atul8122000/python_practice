#######################################
########### Calc_DOB ##################
#######################################
import datetime 
year = int(input("Enter year: "))
month = int(input("Enter Month: "))
day = int(input("Enter Date: "))

date1 = datetime.date(year, month, day)
date2 = datetime.date.today()
res = date2-date1
print(res)