'''
4. ให้เขียนโปรแกรมเพื่อรับข้อมูล 1 บรรทัด ที่ประกอบด้วยจํานวนเต็มหลายจํานวน (คั่นด้วยช่องว่าง)  
ให้ส่งคืนว่ามีจํานวนที่เป็นลบกี่จํานวน โดยใช้ List comprehension 
ให้เขียนในฟังก์ชัน count_minus(str) แล้ว return เป็นคําตอบ 
'''
'''
num_list = [int(num) for num in input().split(' ')]
def count_minus(num_list):
    minus = 0
    for num in range(len(num_list)):
        if num_list[num] < 0:
            minus+=1
    return minus
print(count_minus(num_list))
'''
def count_minus(num_list):
    num_list = [int(i) for i in num_list.split(' ') if int(i)<0]
    minus = 0
    for i in range(len(num_list)):
        minus+=1
    return minus
print(count_minus('10 20 -20 -30'))