'''
7. ให้เขียน function ชื่อ day_of_year(day, month ,year)  
โดยมีการคืนค่า คือ day_of_years เป็นวันที่ลําดับที่เท่าใดของปีคริสตศักราช year 
–  ปีที่เป็น Leap Year เดือนกุมภาพันธ์จะมี 29 วัน  
–  ให้สร้างฟังก์ชัน is_leap เพื่อตรวจสอบ leap year แยกออกมา และให้ฟังก์ชัน day_of_year 
เรียกใช้ is_leap อีกที
'''

def is_leap(year):
    return year%4==0 and (year%100 != 0 or year%400==0)

def day_of_year(day, month, year):
    day_real = 0
    day_from_month = 0
    day_end_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(month-1):
        if is_leap(year):
            day_end_month[1] = 29
        else:
            day_end_month[1] = 28
        day_from_month+=day_end_month[i]
    day_real = day_from_month + day
    return day_real
print(day_of_year(1, 1, 1999))