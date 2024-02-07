import express from "express";
import thaiCutSlim from "thai-cut-slim";
import bodyParser from "body-parser";
import cors from "cors";
import mysql from "mysql2/promise";

import fs from "fs";
import { exec } from "child_process";
import Typo from "typo-js";

const app = express();
app.use(cors());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const pool = await mysql.createConnection({
  host: "nextsoftwarethailand.com",
  user: "nextsoft_dev_01",
  password: "nextsoft1234",
  database: "nextsoft_dev_01",
  port: 3306,
});

app.get("/", (rea, res) => {
  res.send("test API V.1");
});

// POST คำผิด
app.post("/api/check_text", async (req, res) => {
try {

  const { text } = req.body;

  if (text) {
    // delete ข้อมูลก่อนหน้า
    const sqlDelete = `DELETE FROM input_text`;
    const [resultDelete] = await pool.query(sqlDelete);

    if (resultDelete) {
      const sql = `INSERT INTO input_text (text) VALUES (?)`;
      await pool.query(sql, [text]);
      res.status(200).json({ message: "ทำรายการสำเร็จ" });
    }
  }else {
    throw new Error('กรุณากรอกข้อความ')
  }
  
} catch (error) {
  console.log(error);
  res.status(500).json(error.message)

}



  // fs.writeFile("text.txt", text, { encoding: "utf-8" }, (err) => {
  //   if (err) {
  //     console.error(err);
  //     res.status(500).send("เกิดข้อผิดพลาดในการเขียนไฟล์");
  //   } else {
  //     console.log("บันทึกข้อมูลไปยัง text.txt เรียบร้อยแล้ว");

  //     // เรียกใช้ไฟล์ Python spellcheck
  //     exec("python spellcheck2.py", (error, stdout, stderr) => {
  //       if (error) {
  //         console.error(`เกิดข้อผิดพลาด: ${error}`);
  //         return;
  //       }
  //       console.log(`ผลลัพธ์: ${stdout}`);
  //     });

  //     res.status(200).send("บันทึกข้อมูลเรียบร้อยแล้ว");
  //   }
  // });
 
});

// POST คำต้องห้าม
app.post("/api/find_word", async (req, res) => {
  try {
    const { text } = req.body;

    
  if (text) {
    // delete ข้อมูลก่อนหน้า
    const sqlDelete = `DELETE FROM input_text`;
    const [resultDelete] = await pool.query(sqlDelete);

    if (resultDelete) {
      const sql = `INSERT INTO input_text (text) VALUES (?)`;
      await pool.query(sql, [text]);
      res.status(200).json({ message: "ทำรายการสำเร็จ" });
    }
  }else {
    throw new Error('กรุณากรอกข้อความ')
  }


    // fs.writeFile("text.txt", text, { encoding: "utf-8" }, (err) => {
    //   if (err) {
    //     console.error(err);
    //     res.status(500).send("เกิดข้อผิดพลาดในการเขียนไฟล์");
    //   } else {
    //     console.log("บันทึกข้อมูลไปยัง text.txt เรียบร้อยแล้ว");

    //     // เรียกใช้ไฟล์ Python
    //     exec("python findword.py", (error, stdout, stderr) => {
    //       if (error) {
    //         console.error(`เกิดข้อผิดพลาด: ${error}`);
    //         return;
    //       }
    //       console.log(`ผลลัพธ์: ${stdout}`);
    //     });

    //     res.status(200).send("บันทึกข้อมูลเรียบร้อยแล้ว");
    //   }
    // });
  } catch (error) {
    console.log(error);
    res.status(500).json(error.message)
  }
});

// GET ALL คำผิด
app.get("/api/text_wrong", async (req, res) => {
  try {
    const sql = `SELECT id , editword FROM propfthai `;
    const [result] = await pool.query(sql);
    res.status(200).json(result);
  } catch (error) {
    console.log(error);
  }
});

// GET ALL คำต้องห้าม

app.get("/api/find_word", async (req, res) => {
  try {
    const sql = `SELECT * FROM proofstopword ORDER BY startword ASC `;
    const [result] = await pool.query(sql);
    res.status(200).json(result);
  } catch (error) {
    console.log(error);
  }
});

app.post("/api/text", async (req, res) => {
  try {
    const { text } = req.body;

    // โหลดไฟล์พจนานุกรมภาษาไทย
    const dictionary = new Typo("th_TH", null, null, {
      dictionaryPath: "/path/to/th_TH.dic", // ระบุตำแหน่งของไฟล์ .dic ของพจนานุกรมภาษาไทย
      affPath: "/path/to/th_TH.aff", // ระบุตำแหน่งของไฟล์ .aff ของพจนานุกรมภาษาไทย
    });

    // แยกคำจากข้อความ
    const words = text.split(/\s+/);

    const correctedWords = words.map((word) => {
      // ตรวจสอบคำผิด
      const isMisspelled = !dictionary.check(word);

      // ถ้าคำไม่ผิด คืนค่าเดิม
      if (!isMisspelled) {
        return word;
      }

      // ถ้าคำผิด ให้ใช้ suggest() เพื่อหาคำที่ถูกต้อง
      const suggestions = dictionary.suggest(word);
      if (suggestions.length > 0) {
        // เลือกคำแรกในรายการคำที่แนะนำ
        return suggestions[0];
      }

      // ถ้าไม่มีคำแนะนำให้เปลี่ยนแปลง ให้คืนค่าเดิม
      return word;
    });

    const correctedText = correctedWords.join(" ");

    // ส่งข้อความที่แก้ไขแล้วกลับไปยังไคลเอ็นต์
    res.json({ correctedText });
  } catch (error) {
    console.log(error);
    res.status(500).json({ message: "Internal Server Error" });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
