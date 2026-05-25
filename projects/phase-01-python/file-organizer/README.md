# Project 4 — File Organizer

**Phase:** Python Foundations  
**Skills:** `os`, `shutil`, `pathlib`, loops, functions, exception handling

---

## 📋 Project Overview

Build an automation script that:
- Scans a folder for all files
- Organises them into subfolders by file type (Images, Documents, Videos, etc.)
- Logs every move with timestamp
- Can be run on a schedule

---

## 🎯 Business Context

Data analysts frequently receive dumps of files (reports, screenshots, exports) in a single folder.
An organiser script saves hours of manual sorting each week.

---

## 📂 Target Folder Structure (after running)

```text
Downloads/
├── Images/          ← .jpg, .jpeg, .png, .gif, .bmp, .svg
├── Documents/       ← .pdf, .docx, .doc, .xlsx, .pptx, .txt, .csv
├── Videos/          ← .mp4, .mov, .avi, .mkv
├── Audio/           ← .mp3, .wav, .flac
├── Code/            ← .py, .js, .html, .css, .sql, .json
├── Archives/        ← .zip, .tar, .gz, .rar
└── Others/          ← everything else
```

---

## ⚙️ Features to Build

- [ ] Read all files in a source directory (provided as argument or input)
- [ ] Map each file extension to a target folder
- [ ] Move files using `shutil.move()`
- [ ] Skip files already in subfolders (avoid nested moves)
- [ ] Write a log file: `organizer_log.txt` with timestamp + source → destination
- [ ] Print a summary: how many files moved per category

---

## 💡 Hints

1. Use `os.listdir()` or `pathlib.Path.iterdir()` to list files.
2. Use `os.path.splitext(filename)[1].lower()` to get the extension.
3. Use a dictionary to map extensions to folder names.
4. Use `os.makedirs(dest_folder, exist_ok=True)` to create subfolders safely.
5. Add `try/except` around each move in case of permission errors.

---

## 🧪 Testing

Create a folder at `/tmp/test_downloads/` with mixed files:
```bash
touch /tmp/test_downloads/report.pdf
touch /tmp/test_downloads/photo.jpg
touch /tmp/test_downloads/data.csv
touch /tmp/test_downloads/script.py
touch /tmp/test_downloads/video.mp4
```

Run your script and verify the files land in the correct subfolders.
