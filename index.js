import express from "express";
import thaiCutSlim from "thai-cut-slim";
import bodyParser from "body-parser";
import cors from 'cors'

import fs from "fs";

const app = express();
app.use(cors())
app.use(bodyParser.urlencoded({extended:false}))
app.use(bodyParser.json())

app.get('/',(rea,res)=>{
  res.send('test API V.1')
})


app.post("/api/check_text", (req, res) => {
const {text} = req.body
console.log(req.body);

// const textToCheck = 'นี่คือประโยคตัวอย่างที่มีคำที่ถูกต้องและคำที่ผิดพลาด';
const textToCheck = text

// คำที่ต้องการตัด
const wordsToCut = ['อ้วน', 'ผอม'];

// ตัดคำและดึงคำที่ถูกตัดออก
const cutWords = [];
const regexPattern = new RegExp(`(${wordsToCut.join('|')})`, 'g');
const words = thaiCutSlim.cut(textToCheck.replace(regexPattern, (match, p1) => {
  cutWords.push(p1);
  return '';
}));

// ตรวจสอบและแสดงผลลัพธ์
console.log('คำที่ถูกตัดออก:', cutWords.join(', '));
console.log('คำที่เหลือ:', words.join(', '));

res.status(200).json({
    textCut : cutWords,
    textSuccess : words
})


});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
