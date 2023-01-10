'''
2. ให้ตรวจสอบว่า String ที่รับเข้ามาผ่านคีย์บอร์ด เป็นตัวอักษรพิมพ์เล็ก หรือตัวอักษรพิมพ์ใหญ่ อย่างละกี่ตัว 
ให้ตอบ 2 บรรทัด จํานวนตัวพิมพ์เล็ก 1 บรรทัด จํานวนตัวพิมพ์ใหญ่ 1 บรรทัด
'''
sentences = input()
capital_count = 0
small_count = 0
for i in range(0, len(sentences)):
    if 65 <= ord(sentences[i]) <= 90:
        capital_count+=1
    if 97 <= ord(sentences[i]) <= 122:
        small_count+=1
print(small_count)
print(capital_count)