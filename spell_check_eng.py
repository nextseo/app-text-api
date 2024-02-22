import json
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from textblob import TextBlob

def spell_check_eng(text):
    if text.strip() != '':
        a = text.strip()          # incorrect spelling
        b = TextBlob(a)
        txt = str(b.correct())
        # prints the corrected spelling
        print(txt)
        
        return b
    else:
        return {'result': 'error', 'message': 'กรุณากรอกข้อความ'}


if __name__ == "__main__":
    example_text = sys.argv[1]  # รับข้อความจาก command line arguments
    # print(example_text)
    #example_text='Spelling cmputr watr'
    result = spell_check_eng(example_text)
    # print(json.dumps(result))
    