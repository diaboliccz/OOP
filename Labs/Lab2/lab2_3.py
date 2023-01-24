'''
3. กําหนดให้ List x เป็น List ของจํานวนเต็ม  
ให้เขียนโปรแกรมเพื่อลบจํานวนเต็มทุกตัวใน x ที่มีค่าเป็นลบ โดยใช้ List comprehension 
–  เช่น x = [ [1, -3, 2], [-8, 5], [-1, -4, -3] ] 
–  ได้คําตอบเป็น [ [1, 2], [5], [] ] 
ให้สร้างเป็น delete_minus(x) แล้ว return เป็น List คําตอบ
'''
'''
x = [[1, -3, 2], [-8, 5], [-1, -4, -3]]
def delete_minus(x):
    x_new = []
    for i in range(len(x)):
        x_new.append([])
        for j in range(len(x[i])):
            if x[i][j] > 0:
                x_new[i].append(x[i][j])
    return x_new
print(delete_minus(x))
'''

x = [[1, -3, 2], [-8, 5], [-1, -4, -3]]
def delete_minus(x):
    x_new = [[x[i][j] for j in range(len(x[i])) if x[i][j] >= 0]for i in range(len(x))]
    return x_new
print(delete_minus(x))