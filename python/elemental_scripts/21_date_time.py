# date_time.py
# ---------
# Updated: cramos 27/set/2022
# 
# This is a basic example of how to use DateTime library

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
#day = now.
#hour = 

print(f'Year: {year}, Month: {month}, weekday: \n')

day_of_week = now.weekday()
print(f'day_of_week: {day_of_week} [0:mon, 1:tue, 2:wed, 3:thu, 4:fri, 5:sat, 6:sun] \n')

# Print string formated date
current_date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
print(f'current_date_time_str: {current_date_time_str} \n')
	
# Set date time
my_start_date = dt.datetime(year=2022, month=11, day=15, hour=18, minute=58, second=33)
print(f'my_start_date: {my_start_date} \n')
