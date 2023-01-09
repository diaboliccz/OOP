'''
2. ให้ตรวจสอบว่า String ที่รับเข้ามาผ่านคีย์บอร์ด เป็นตัวอักษรพิมพ์เล็ก หรือตัวอักษรพิมพ์ใหญ่ อย่างละกี่ตัว 
ให้ตอบ 2 บรรทัด จํานวนตัวพิมพ์เล็ก 1 บรรทัด จํานวนตัวพิมพ์ใหญ่ 1 บรรทัด
'''
char = input()
capital_Count = 0
small_Count = 0
for i in range(0, len(char)):
    if 65 <= ord(char[i]) <= 90:
        capital_Count+=1
    if 97 <= ord(char[i]) <= 122:
        small_Count+=1
print(small_Count)
print(capital_Count)