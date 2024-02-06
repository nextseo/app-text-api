import pythainlp
from pythainlp.tokenize import Tokenizer
from pythainlp.spell import NorvigSpellChecker

# ฟังก์ชันแก้ไขคำภาษาไทยที่ผิด
def correct_thai_words(text):
    # ใช้โมเดล Tokenizer เพื่อตัดคำ
    tokenizer = Tokenizer()
    words = tokenizer.word_tokenize(text)
    
    # ใช้โมเดล NorvigSpellChecker เพื่อแก้คำที่ผิด
    spell_checker = NorvigSpellChecker()
    corrected_words = [spell_checker.correct(word) for word in words]
    
    # รวมคำที่แก้ไขแล้วกลับเป็นข้อความ
    corrected_text = ''.join(corrected_words)
    return corrected_text

# เปิดไฟล์ input.txt ในโหมดอ่าน ('r') และ encoding เป็น 'utf-8'
with open('input.txt', 'r', encoding='utf-8') as file:
    # อ่านข้อมูลจากไฟล์
    thai_text = file.read()

# แก้ไขคำภาษาไทยที่ผิด
corrected_text = correct_thai_words(thai_text)

# เขียนข้อมูลที่แก้ไขแล้วลงในไฟล์ output.txt
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(corrected_text)

print("แก้ไขคำภาษาไทยที่ผิดแล้วบันทึกลงในไฟล์ output.txt")