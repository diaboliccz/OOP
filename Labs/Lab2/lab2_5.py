'''
5. ให้เขียนโปรแกรมเพื่อรับ string 1 ตัว  
ให้ส่งคืนเฉพาะตัวอักษรที่เป็นภาษาอังกฤษ โดยใช้ List comprehension 
ให้เขียนในฟังก์ชัน only_english(string1) แล้ว return เป็นคําตอบเป็น string
'''
'''
word = input()
def only_english(string1):
    string1 = []
    for i in range(len(word)):
        if (65 <= ord(word[i]) <= 90 or 97 <= ord(word[i]) <= 122):
            string1.append(word[i])
    for i in range(len(string1)):
        print(string1[i], end='')
only_english(word)
'''
def only_english(word):
    string1 = [word[i] for i in range(len(word)) if word[i].isalpha()]
    string1 = ''.join(string1[i] for i in range(len(string1)))
    return string1
print(only_english('abcd666999bbf'))