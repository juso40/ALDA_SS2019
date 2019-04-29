import time
from datetime import date
from datetime import timedelta


'''Nr2. a)
Das Jahr kann mit Montag bis Sonntag beginnen (7 verschiedene Möglichkeiten)
Dies multipliziert mit 2, weil es auch Schaltjahre gibt.
->Es gibt 14 verschiedene Möglichkeiten
'''

def friday13th():
    count=0
    monate=[31,28,31,30,31,30,31,31,30,31,30,31]
    for wdays in range(7):
        for schaltjar in [True,False]:
            if schaltjar:
                monate[1]=29
            else:
                monate[1]=28
            for monat in range(12):
                for days in range(1,monate[monat]):
                    if days==13 and wdays==4:
                        count+=1
    print(count)

friday13th()


#Nr2. c)
def friday13thSince(day, month, year):
    START_YEAR = date(year, month, day)
    START_COPY = START_YEAR
    TODAY = date.today()
    friday13Counter = 0
    while START_YEAR <= TODAY:
        if(START_YEAR.isoweekday()!=5):
            START_YEAR = START_YEAR + timedelta(days=1)
        elif(START_YEAR.isoweekday()==5):
            if( START_YEAR.day == 13):
                friday13Counter+=1
            START_YEAR = START_YEAR + timedelta(weeks=1)  #increase by one week
    print("Since",START_COPY,"were",friday13Counter,"friday the 13th!")

def inputBDay():
    while True:
        try:
            year = int(input("Please Enter your Birthday\nYear:"))
            month = int(input("Month:"))
            day = int(input("Day:"))
            friday13thSince(day,month,year)
            break
        except:
            print("\nThat is not a valid Date!")

inputBDay()
