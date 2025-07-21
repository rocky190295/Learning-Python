#  File Organizer (Python)

A fully modular file organization utility that helps you clean up any folder (ex: Downloads) by sorting files either:
- By file type (Like PDF, JPG, DOCX ...)
- By Date modified (Oorganized into Year/Month folders)

Designed with reusability and future GUI integration in mind

# Tech stack

| Module                 | Purpose                                |
|------------------------|----------------------------------------|
| os                     | File system navigation, path operations|
| shutil                 | Move files between folder              |
| datetime               | Get modified timestamps                |
| sys                    | Exits and valdations                   |
| collections.defaultdict| Efficient counting/summarizing         |
---

##  Features
- Organize files by type (file extension)
- irganize file by modification date (year/Month)
- Automatically create necessary folders
- Skip  folders and only process file
- Provide file summaries before taking action
- Modular, reuable code - ready for GUI apps or automation

---

## Organizing by file type
#### Before running the script 
Downloads/
├── resume.docx
├── photo.jpg
├── report.pdf
├── archive.zip

#### After Running the scripts
Downloads/
├── DOCX/
│ └── resume.docx
├── JPG/
│ └── photo.jpg
├── PDF/
│ └── report.pdf
├── ZIP/
│ └── archive.zip

---

## 🧰 How to Run

1. Open terminal / command prompt
2. Run the script:

```bash
python file_organizer.py
