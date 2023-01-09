'''
5. ตัวเลข palindrome คือตัวเลขที่อ่านได้ทั้ง 2 ทาง แล้วมีค่าเท่ากัน เช่น 9009 โดย 9009 คือ palindrome 
ที่เกิดจากการคูณของตัวเลข 2 หลักที่มากที่สุด คือ 91x99 จงหา palindrome ที่มากที่สุดของตัวเลข 3 
หลัก
100*100 ถึง 999*999 อยู่ในช่วง [100000, 999999]
จะได้ว่าสามารถเขียนผลคูณพาลินโดรมได้ในรูป 
ABCCBA => ABCCBA = A(10^5+1) + B(10^4+10) + C(10^3+10^2)
          ABCCBA = A(100001) + B(10010) + C(1100) เมื่อ A ∈ [1,9] , B,C ∈ [0, 9]
'''
result1 = []
result2 = []
result3 = []
import math
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            num = a*(100001)+b*(10010)+c*(1100)
            for i in range(100, 1000):
                if num%i == 0 and num/i < 1000:
                    result1.append(i)
                    result2.append(num/i)
                    result3.append(num)
                    #print(f'{i} * {num/i} = {num}')
print(max(result3))