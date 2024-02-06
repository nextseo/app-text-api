import thaispellcheck
import mysql.connector
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#####################
mydb = mysql.connector.connect(
    host="nextsoftwarethailand.com",
    user="nextsoft_dev_01", 
    passwd="nextsoft1234",
    database="nextsoft_dev_01",
    allow_local_infile=True,
    port = 3306
    )

mycursor = mydb.cursor()

try:
  mycursor.execute("DELETE FROM propfthai")
  print('All rows are deleted.')
except:
  print('An exception occurred while deleting rows.')

mydb.commit()
#####################
#####################

# เปิดไฟล์เพื่ออ่าน
with open('text.txt', 'r', encoding='utf-8') as file:
    # อ่านข้อมูลทั้งหมดจากไฟล์
    thai_text = file.read()
    
print('thai_text',thai_text)

import thaispellcheck
print(thaispellcheck.check(thai_text,autocorrect=True))

a = thaispellcheck.check(thai_text,autocorrect=True)
print(a)

yy=0
#####################
mydb = mysql.connector.connect(
    host="nextsoftwarethailand.com",
    user="nextsoft_dev_01", 
    passwd="nextsoft1234",
    database="nextsoft_dev_01",
    allow_local_infile=True,
    port = 3306
    )

mycursor = mydb.cursor()
sql = "INSERT INTO propfthai (yy,editword) VALUES (%s,%s)"
val = (yy,a)
mycursor.execute(sql, val)
mydb.commit() 
print(mycursor.rowcount, "record inserted propfthai.")  

