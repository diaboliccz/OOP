'''
6. จงเขียนโปรแกรมแสดงรูปสามเหลื่ยม (ตามโปรแกรมใน Slide 5) แต่ปรับปรุงให้ใช้ Loop เพียง Loop เดียว
'''

n=10
loop_total = n*n+n
for i in range(0, loop_total):
    row = i//n
    col = i%(n+1)
    if col == n:
        print("#", end = '\n')
    else:
        if row+col > n-1:
            print("#", end = '')
        else:
            print(" ", end = '')