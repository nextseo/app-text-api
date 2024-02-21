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

const pool = mysql.createPool({
  host: "nextsoftwarethailand.com",
  user: "nextsoft_app_text",
  password: "nextsoft1234",
  database: "nextsoft_app_text",
  port: 3306,
});

app.get("/", (rea, res) => {
  res.send("test API V.1");
});

//  // เรียกใช้ไฟล์ Python spellcheck
//  exec("python spellcheck2.py", (error, stdout, stderr) => {
//   if (error) {
//     console.error(`เกิดข้อผิดพลาด: ${error}`);
//     return;
//   }
//   console.log(`ผลลัพธ์: ${stdout}`);
//   if (stdout) {
//     res.status(200).json({message : 'ทำรายการสำเร็จ'});
//   }
// });

// POST คำผิด
app.post("/api/check_text", async (req, res) => {
  try {
    const { text } = req.body;

    if (text) {
      exec(`python  spellcheck2.py "${text}"`, (error, stdout, stderr) => {
        if (error) {
          console.error(`exec error: ${error}`);
          res.status(500).json(error.message);
          return;
        }
        if (stdout) {
          console.log(stdout);
          res.status(200).json(stdout.trim());

          // data: "ผมอ้วนมาก\r\n" อยากได้แค่ข้อความ
        }
      });
    } else {
      throw new Error("กรุณากรอกข้อความ");
    }
  } catch (error) {
    console.log(error);
    res.status(500).json(error.message);
  }
});

// POST คำต้องห้าม
app.post("/api/find_word", async (req, res) => {
  try {
    const { text } = req.body;

    if (text) {
      // delete ข้อมูลก่อนหน้า
      const sqlDelete = `DELETE FROM input_text`;
      const [resultDelete] = await pool.query(sqlDelete);

      // DELETE TABLE proofstopword
      const [resultDelete_2] = await pool.query("DELETE FROM proofstopword");

      if (resultDelete_2) {
        const sql = `INSERT INTO input_text (text) VALUES (?)`;
        await pool.query(sql, [text]);

        //     // เรียกใช้ไฟล์ Python
        exec("python findword.py", (error, stdout, stderr) => {
          if (error) {
            console.error(`เกิดข้อผิดพลาด: ${error}`);
            return;
          }
          console.log(`ผลลัพธ์: ${stdout}`);
          if (stdout) {
            res.status(200).send("บันทึกข้อมูลเรียบร้อยแล้ว");
          }
        });
      }
    } else {
      throw new Error("กรุณากรอกข้อความ");
    }
  } catch (error) {
    console.log(error);
    res.status(500).json(error.message);
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

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
