import datetime

x = datetime.datetime.now()


print(x)
print(x.strftime("%A"))    # return day name sun , mon etc  

print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)

# output
"""
2024-05-18 09:54:04.781249
2024
5
18
9
54
4
"""

print(type(x))   #==============+++> <class 'datetime.datetime'>
print(type(x.year))  #===================>> <class 'int'>

# month hour dayetc sab int honge 




##################################    how to create a date by ourself =========================

y = datetime.datetime(2020,   5,   17 ,12 ,   8 ,  55 )
##################### year  month day hour minute sec
print(y)




""""


val =   x.strftime("%w")

all possible params and there use 

%a 	Weekday, short version 	Wed 	
%A 	Weekday, full version 	Wednesday 	
%w 	Weekday as a number 0-6, 0 is Sunday 	3 	
%d 	Day of month 01-31 	31 	
%b 	Month name, short version 	Dec 	
%B 	Month name, full version 	December 	
%m 	Month as a number 01-12 	12 	
%y 	Year, short version, without century 	18 	
%Y 	Year, full version 	2018 	
%H 	Hour 00-23 	17 	
%I 	Hour 00-12 	05 	
%p 	AM/PM 	PM 	
%M 	Minute 00-59 	41 	
%S 	Second 00-59 	08 	
%f 	Microsecond 000000-999999 	548513 	
%z 	UTC offset 	+0100 	
%Z 	Timezone 	CST 	
%j 	Day number of year 001-366 	365 	
%U 	Week number of year, Sunday as the first day of week, 00-53 	52 	
%W 	Week number of year, Monday as the first day of week, 00-53 	52 	
%c 	Local version of date and time 	Mon Dec 31 17:41:00 2018 	
%C 	Century 	20 	
%x 	Local version of date 	12/31/18 	
%X 	Local version of time 	17:41:00 	
%% 	A % character 	% 	
%G 	ISO 8601 year 	2018 	
%u 	ISO 8601 weekday (1-7) 	1 	
%V 	ISO 8601 weeknumber (01-53) 	01



"""