import calendar
date = input()
month, day, year = map(int, date. split())
n=(calendar.weekday(year,month,day))
if n==0:
 print("MONDAY")
elif n==1:
    print("TUESDAY")
elif n==2:
    print("WEDNESDAY")
elif n==3:
    print("THURSDAY")
elif n==4:
    print("FRIDAY")
elif n==5:
    print("SATURDAY")
else:
    print("SUNDAY")

