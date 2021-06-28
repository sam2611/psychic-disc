'''from collections import namedtuple
total=0
n=int(input())
student = namedtuple('s','ID MARKS NAME CLASS')
list1=[]
for i in range(0,n):
     ID, MARKS, NAME, CLASS = input().split()
     s= student(ID, MARKS, NAME, CLASS)
     total+=int(s.MARKS)

print(total/n)'''

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

