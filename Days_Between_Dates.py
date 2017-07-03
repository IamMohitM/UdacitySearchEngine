import calendar

# """def ifLeapYear(year):
#     if year%400==0:
#         return True#366
#     elif year % 100==0:
#         return False#365
#     elif year%4==0:
#         return True#366
#     return False#365"""


def days_year(year):
    if calendar.isleap(year):
        return 366
    else:
        return 365

def date1_before_date2(year1,month1,day1,year2,month2,day2):
    if year1<year2:
        return True
    elif year2==year1:
        if month1<month2:
            return True
        elif month2==month1:
            if day1<day2:
                return True
    return False

def days_in_month(year,month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month==2:
        if calendar.isleap(year):
            return 29
        else:
            return 28
    else:
        return 30
"""
def next_day(year,month,day):
    if day<days_in_month(year,month):
        return year,month,day+1
    else:
        if days_in_month(year,month)==day:
            if month==12:
                return year+1,1,1
            return year,month+1,1"""

def days_left_year(year,month,day):
    "This method returns the days left in the year."
    mo=1
    count=0
    y=days_year(year)
    while(mo<month):
        count=count+days_in_month(year,mo)
        mo+=1
    count+=day
    return y-count

def diff_months(year1,month1,day1,month2,day2):
    """This method is only executed if the months are in the same year."""
    days=0
    m=month1
    while (m <= month2):
        if m == month1:
            days = days + days_in_month(year1, month1) - day1
        elif m == month2:
            days = days + day2
            return days
        else:
            days = days + days_in_month(year1, m)
        m=m+1
    return days

"""Most efficient method."""
def count_day(year1,month1,day1,year2,month2,day2):
    y=year1+1
    days=0
    if date1_before_date2(year1,month1,day1,year2,month2,day2):
        if year1<year2:
            days = days_left_year(year1, month1, day1)
        else:
            if month1==month2:
                return day2-day1
            else:
                days=diff_months(year1,month1,day1,month2,day2)
                return days
        while(y<year2):
            days+=days_year(y)
            y+=1
        days+=(days_year(year2)-days_left_year(year2,month2,day2))
    return days

"""The method below is very ineffecient"""
"""def count_days(year1,month1,day1,year2,month2,day2):
    days=0
    while date1_before_date2(year1,month1,day1,year2,month2,day2):
        days=days+1
        year1,month1,day1=next_day(year1,month1,day1)
    return days"""

#print days_left_year(2012,12,25)
#print count_day(2016,12,1,2017,2,25)
print count_day(2017,3,4,20170,3,5)

#print count_day(1997,3,4,200000,1,19)
#print count_days(1997,3,4,20000,1,19)