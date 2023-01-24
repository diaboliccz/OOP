'''
8. จากโปรแกรมในข้อ 7 ให้เขียนฟังก์ชัน เพิ่มเติมเป็น date_diff  
–  รับข้อมูลในรูปแบบ “dd-mm-yyyy” เช่น  
date_diff(“1-1-2018”, “1-1-2020”) จะได้ 731 วัน 
date_diff(“25-12-1999”, “9-3-2000”) จะได้ 76 วัน 
–  ให้เขียนฟังก์ชัน day_in_year โดยจะส่งค่าจํานวนวันของปี (365 หรือ 366) โดยรับข้อมูลเป็น ปี  
–  ส่งคืนข้อมูลเป็นจํานวนวันตั้งแต่วันที่แรก จนถึงวันที่สอง โดยรวมทั้ง 2 วันนั้นเข้าไปด้วย  
–  ให้สมมติว่าวันแรก จะต้องมาก่อนวันที่สองเสมอ ดังนั้นไม่ต้องตรวจสอบ
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
    
    for i in range(year1, year2+1):
        day_from_year += day_in_year(i)
    
    day_1_from_start = day_of_year(day1, month1, year1)
    day_2_to_the_end = day_in_year(year2) - day_of_year(day2, month2, year2)
    day_diff = day_from_year - (day_1_from_start + day_2_to_the_end) + 1
    return day_diff
print(date_diff("25-12-1999", "9-3-2000"))