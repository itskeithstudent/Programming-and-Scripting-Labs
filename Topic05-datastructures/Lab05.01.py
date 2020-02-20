#Add all months to tuple list
months_tuple = ("January","February","March","April","May","June","July","August","September","October","November","December")
#assign months 4,5 and 6 to summer_months_tuple
summer_months_tuple = months_tuple[4:7]
#trying out list comprehension to do as oneliner
[print(x) for x in summer_months_tuple]

###print todays day or month
import datetime

todays_date = datetime.datetime.today()
print(todays_date.strftime('%A')) # print todays day
print(todays_date.strftime('%b')) # print todays month

#more intuitive solution
import calendar
print(calendar.day_name[todays_date.weekday()])
#print(calendar.month_name[todays_date.month()])
