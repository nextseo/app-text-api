import thaispellcheck
import numpy as np
import mysql.connector
from PIL import Image
from PIL import Image as Img
from PIL import Image, ImageFont, ImageDraw
from PIL import ImageFont, ImageDraw, Image
#text = "เราไปโรงเรยนกัน"

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
with open('text.txt',encoding="utf8") as f:
    lines = f.readlines()
    print('lineslines',len(lines[0]))
    print('linesss',lines)
    print('lines',lines[0])
    
text = lines[0]

print(thaispellcheck.check(text))

print(thaispellcheck.check(text,autocorrect=True))

xx = thaispellcheck.check(text,autocorrect=True)
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
val = (yy,xx)
mycursor.execute(sql, val)
mydb.commit() 
print(mycursor.rowcount, "record inserted SCB_database.")  
                   