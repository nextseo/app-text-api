import thaispellcheck
import mysql.connector
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#####################
mydb = mysql.connector.connect(
    host="nextsoftwarethailand.com",
    user="nextsoft_app_text", 
    passwd="nextsoft1234",
    database="nextsoft_app_text",
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

sql_select_Query = "select * from input_text"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
# get all records
records = cursor.fetchall()
# print("Total number of rows in table: ", cursor.rowcount)
# print("\nPrinting each row")
for row in records:
    thai_text = row[1] #set notification
    
print('thai_text',thai_text)
    
#####################
'''
# เปิดไฟล์เพื่ออ่าน
with open('text.txt', 'r', encoding='utf-8') as file:
    # อ่านข้อมูลทั้งหมดจากไฟล์
    thai_text = file.read()
    
print('thai_text',thai_text)
'''
import thaispellcheck
print(thaispellcheck.check(thai_text,autocorrect=True))

a = thaispellcheck.check(thai_text,autocorrect=True)
print(a)

yy=0
#####################
mydb = mysql.connector.connect(
    host="nextsoftwarethailand.com",
    user="nextsoft_app_text", 
    passwd="nextsoft1234",
    database="nextsoft_app_text",
    allow_local_infile=True,
    port = 3306
    )

mycursor = mydb.cursor()
sql = "INSERT INTO propfthai (yy,editword) VALUES (%s,%s)"
val = (yy,a)
mycursor.execute(sql, val)
mydb.commit() 
print(mycursor.rowcount, "record inserted propfthai.")  

