'''
6. จงเขียนโปรแกรมแสดงรูปสามเหลื่ยม (ตามโปรแกรมใน Slide 5) แต่ปรับปรุงให้ใช้ Loop เพียง Loop เดียว
'''

import math
num = 7
length = 2*(num)+2
total = num*length
for i in range(1, total):
    row = i//length
    col = i%length
    if i%length==0:
        print('\n', end = '')
    else:
        if num%2==0:
            if num+1-(row+1)<col<num+1+(row+1) and abs(col-row)%2!=0:
                print("#", end = '')
            else:
                print(' ', end = '')
        else:
            if num+1-(row+1)<col<num+1+(row+1) and abs(col-row)%2==0:
                print("#", end = '')
            else:
                print(' ', end = '')