'''
9. จากโปรแกรมในข้อ 8 ให้เขียนฟังก์ชัน date_diff  เพิ่มเติม โดยให้มีการตรวจสอบ  
–  วันที่ต้องเป็นวันที่ถูกต้องของเดือนนั้นๆ  
–  เดือนต้องอยู่ระหว่าง 1-12  
–  เดือนกุมภาพันธ์ของปีที่มี Leap Year เท่านั้นที่จะมี 29 วันได้  
–  หากข้อมูล Input ผิดพลาด ให้ Return -1
'''

def is_leap(year):
    return year%4==0 and (year%100 != 0 or year%400==0)

def day_in_year(year):
    if is_leap(year):
        return 366
    return 365

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

def day_check(day, month, year):
    if year>=1 and 1<=month<=12 and day>=1:
        if ((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and 1<=day<=31) or ((month == 4 or month == 6 or month == 9 or month == 11)):
            return True
        elif month == 2:
            if is_leap(year):
                if 1<=day<=29:
                    return 1
            else:
                if 1<=day<=28:
                    return 1

def date_diff(day_first, day_second):
    day_diff = 0
    day_from_year = 0
    
    day_first = day_first.split('-')
    day1 = int(day_first[0])
    month1 = int(day_first[1])
    year1 = int(day_first[2])
    
    day_second = day_second.split('-')
    day2 = int(day_second[0])
    month2 = int(day_second[1])
    year2 = int(day_second[2])
    
    if day_check(day1, month1, year1) and day_check(day2, month2, year2):
        pass
    else:
        return -1
    
    for i in range(year1, year2+1):
        day_from_year += day_in_year(i)
    
    day_1_from_start = day_of_year(day1, month1, year1)
    day_2_to_the_end = day_in_year(year2) - day_of_year(day2, month2, year2)
    day_diff = day_from_year - (day_1_from_start + day_2_to_the_end) + 1
    return day_diff
print(date_diff("29-2-1999", "29-2-2004"))