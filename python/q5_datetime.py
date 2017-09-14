# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

date_format1 = '%m-%d-%Y'
s1 = datetime.strptime(date_start, date_format1)
e1 = datetime.strptime(date_end, date_format1)

days_between1 = (e1-s1).days
print(days_between1)

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_format2 = '%m%d%Y'
s2 = datetime.strptime(date_start, date_format2)
e2 = datetime.strptime(date_end, date_format2)

days_between2 = (e2-s2).days
print(days_between2)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_format3 = '%d-%b-%Y'
s3 = datetime.strptime(date_start, date_format3)
e3 = datetime.strptime(date_end, date_format3)

days_between3 = (e3-s3).days
print(days_between3)
