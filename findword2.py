from pythainlp import word_tokenize
import sys
import io
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#####################
#####################
stopwordgroup = ['อ้วน',
    'ผอม',
    'ระเบิดไขมัน',
    'ไซซ์ใหญ่',
    'ไซส์ใหญ่',
    'ลดน้ำหนัก',
    'ไม่โยโย่',
    'ขาแขนใหญ่',
    'ดื้อยา',
    'ยา',
    'ได้ผล 100%',
    'ได้ผลร้อยเปอร์เซ็นต์',
    'เห็นผล',
    'คำที่ส่งผลต่อจิตใจ',
    'ลดด่วน',
    'อยากผอม',
    'ผอม',
    'ผอมทันใจแน่นอน',
    'แน่นอน',
    'เห็นผลตั้งแต่ครั้งแรกที่ใช้',
    'เห็นผล',
    'เบิร์น',
    'สลายไขมัน',
    'หุ่นดีกว่าเดิม',
    'หุ่นดี',
    'การันตี',
    'ผลลัพธ์',
    'ดีกว่า',
    'ยินดีคืนเงิน',
    'รับประกัน',
    'รักษาโรค',
    'ป้องกันโรค',
    'เพิ่มสมรรถภาพทางเพศ',
    'ปรับรูปหน้า',
    'วิเศษ',
    'ยอดเยี่ยม',
    'มหัศจรรย์',
    'เลิศที่สุด',
    'ปาฏิหาริย์วิเศษ',
    'ปาฏิหาริย์',
    'มหัศจรรย์',
    'ดีเลิศ',
    'ชนะเลิศ',
    'ชั้นเลิศ',
    'เลิศเลอ',
    'ล้ำเลิศ',
    'ยอดเยี่ยม',
    'ยอดไปเลย',
    'เยี่ยมยอด',
    'เยี่ยมไปเลย',
    'เยี่ยมสุดๆ',
    'สุดยอด',
    'ที่เหนึ่ง',
    'หนึ่งเดียว',
    'ที่หนึ่งเลย',
    'ที่สุด',
    'ดีที่สุด',
    'ดีเด็ด',
    'สูงสุด',
    'เด็ดขาด',
    'หายห่วง',
    'หายขาด',
    'ไม่มีผลค้างเคียง',
    'อย.',
    'รับรอง',
    'เห็นผลเร็ว',
    'เห็นผลไว',
    'รักษา',
    'บรรเทา',
    'ฆ่าเชื้อแบคทีเรีย',
    'ฆ่าเชื้อ',
    'ป้องกันการเกิดสิว',
    'ป้องกัน',
    'รักษาโรคผิวหนัง',
    'รักษาโรค',
    'ขาวไว',
    'ขาวทันที',
    'ต้านอนุมูลอิสระ',
    'ธรรมชาติ 100%',
    'ธรรมชาติร้อยเปอร์เซ็นต์',
    'ลดรอยแดง',
    'ลดรอยดำ',
    'ลดรอยสิว',
    'ลดผ้ากระ',
    'ลด',
    'สลายผ้า',
    'สลาย',
    'เห็นผล',
    'ภายใน',
    'จริง',
    'หน้าเรียว',
    'รับประกัน',
    'การันตี',
    'กระชับ',
    'สัดส่วน',
    'ไม่เห็นผลยินดีคืนเงิน',
    'ยินดีคืนเงิน',
    'ขาย',
    'ขาว',
    'ไม่อันตราย',
    'ปลอดภัย',
    'รีวิว',
    'เห็นผล',
    'ผลลัพท์ชัดเจน',
    'แบรนด์เดียวในไทย',
    'ประเทศไทย',
    'วันละ',
    'โปรโมชั่น',
    'แถมฟรี',
    'ออเดอร์',
    'ส่งของ',
    'เพียว',
    'สลิม',
    'Slim',
    'หุ่นเป๊ะ',
    'ผอมด่วน',
    'ถาวร',
    'ดื้อ',
    'ยา',
    'อ่อนกว่าไว',
    'แก้',
    'ช่วยให้',
    'กันแดด',
    'ท้าแดด',
    'ดับกลิ่น',
    'กระชับ',
    'กระจ่างใส',
    'นุ่ม',
    'เด้ง',
    'เปล่งปลั่ง',
    'ออร่า',
    'เปล่งประกาย',
    'คำพูดอ้างอิทธิฤทธิ',
    'ปาฏิหาริย์',
    'ถูกหวย',
    'รวย',
    'เสี่ยงดวง',
    'เสี่ยงโชค',
    'พลิกชีวิต',
    'ดีกว่า',
    'เปลี่ยนโชคชะตา',
    'ศักดิ์สิทธิ์',
    'ศรัทธา',
    'เลื่อมใส',
    'สรรพคุณ',
    'เหนือ',
    'รวย',
    'วิธีรวยเร็ว',
    'ร่ำรวย',
    'ทำงานที่บ้านก็รวยได้',
    'ทำงานประจำทำแล้วไม่รวย',
    'ขายวันนี้ พรุ่งนี้รวย',
    'งานสบาย',
    'รวยเร็ว',
    'ใช้สิทธิ',
    'สิทธิพิเศษ',
    'รวยง่ายๆ',
    'รวยง่าย',
    'ได้เงินเร็ว',
    'เงินไว',
    'รวยแบบไม่ทันตั้งตัว',
    'รวยชั่วข้ามคืน',
    'รวยในข้ามคืน',
    'แค่ขายก็รวยแล้ว',
    'ซื้อเลย',
    'ลิงค์',
    'กัญชา',
    'ยา',
    'อาหารเสริม',
    'ใบสั่ง',
    'แพทย์',
    'อาวุธ',
    'ปืน',
    'มีด',
    'สเปรย์พริกไทย',
    'สเปรย์',
    'ระเบิด',
    'ดอกไม้ไฟ',
    'พุ',
    'โควิด',
    'ไวรัส',
    'เชื้อโรค',
    'บุหรี่',
    'ยาสูบ',
    'ซิการ์',
    'กล้องยาสูบ',
    'ฮุคคา',
    'บาร์',
    'เหล้า',
    'สุรา',
    'บุหรี่ไฟฟ้า',
    'เซ็กส์',
    'ถุงอนามัย',
    'แอบถ่าย',
    'ดักฟัง',
    'ปลอม',
    'เงินดีจิตอล',
    'เชื้อ',
    'หวย',
    'สายเทา',
    'สายดำ',
    'ได้',
    'เหี่ย',
    'สัตว์',
    'หมา',
    'ควย',
    'หี',
    'อี',
    'ไอ้',
    'เวร',
    'เวณ',
    'ปรับสมดุล',
    'ฟื้นฟู',
    'เพิ่มน้ำนม',
    'กระตุ้น',
    'เพิ่มน้ำนม',
    'บำรุงสมอง',
    'บำรุงประสาท',
    'เสริมสร้าง',
    'ภูมิคุ้มกัน',
    'ล้างสารพิษ',
    'ล้างลำไส้',
    'ล้าง',
    'ปรับสายตา',
    'ขับน้ำ',
    'ช่วย',
    'กรอบหน้าชัด',
    'เสริมสร้าง',
    'สมรรถภาพทางเพศ',
    'เพศ',
    'อาหารเสริม',
    'ประสิทธิภาพ',
    'หลั่ง',
    'ลดอาการ',
    'เพิ่มขนาด',
    'อัพไซส์',
    'กระชับ',
    'ปลุก',
    'อึด',
    'ทน',
    'ไว',
    'กระตุ้น',
    'คืนความเป็นหนุ่ม',
    'คืนความเห็นสาว',
    'ฆ่าเชื้อ',
    'เห็นผล']

def word_check(text):
    mytext = text
    dd = []
    for xstop in range(0,len(stopwordgroup)):
            startword = mytext.find(stopwordgroup[xstop])
            if startword>=0:
                # print('stopwordgroup[xstop]',stopwordgroup[xstop])
                lenstr = len(stopwordgroup[xstop])
                endword = startword+lenstr
                dd.append({"start": startword, "end": endword})
    
    dd = sorted(dd, key=lambda x: (x["start"], x["end"]))
    return dd
    
if __name__ == "__main__":
    #example_text = sys.argv[1]  # รับข้อความจาก command line arguments
    # print(example_text)
    example_text = 'กระตุ้นสมองให้ไวด้วยการเพิ่มขนาด'
    result = word_check(example_text)
    output_json = json.dumps(result)
    print(output_json)
    
   # Convert each dictionary to a string without quotes around keys
    # output = '[' + ', '.join([f'{{start:{item["start"]}, end:{item["end"]}}}' for item in result]) + ']'
    # output_json = json.dumps(output)
    # print(output_json)
