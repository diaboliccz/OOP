'''
4. จงเขียนโปรแกรมที่คํานวณค่าของ a+aa+aaa+aaaa เมื่อรับข้อมูลเป็นตัวเลข 1 หลัก  
Input : 9 Output : 11106 (=9+99+999+9999)
A+AA+AAA+AAAA = A+[A(10)+A]+[A(100)+A(10)+A]+[A[1000]+A[100]+A[10]+A]
              = A*1000 + 200*A + 30*A + 4*A
'''

num = int(input())
result = num*1000 + 200*num + 30*num + 4*num
print(result)