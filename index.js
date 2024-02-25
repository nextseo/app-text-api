import express from "express";
import bodyParser from "body-parser";
import cors from "cors";
import { exec } from "child_process";

const app = express();
app.use(cors());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get("/", (rea, res) => {
  res.send("test API V.2");
});

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
      exec(`python  findword2.py "${text}"`, (error, stdout, stderr) => {
        if (error) {
          console.error(`exec error: ${error}`);
          res.status(500).json(error.message);
          return;
        }
        if (stdout) {
          // console.log(stdout);
          const Newdata = JSON.parse(stdout);

          const uniqueData = Newdata.filter(
            (item, index, self) =>
              index ===
              self.findIndex(
                (t) => t.start === item.start && t.end === item.end
              )
          );

          res.status(200).json(uniqueData);
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

// ภาษาอังกฤษ english
app.post("/api/english", async (req, res) => {
  try {
    const { text } = req.body;

    if (text) {
      exec(`python  spell_check_eng.py "${text}"`, (error, stdout, stderr) => {
        if (error) {
          console.error(`exec error: ${error}`);
          res.status(500).json(error.message);
          return;
        }
        if (stdout) {
          console.log(stdout);
          res.status(200).json(stdout.trim());
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

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
