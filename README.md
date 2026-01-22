# File Organizer 🗂️

A clean, modern desktop application that automatically sorts files in any folder by their type — with a beautiful Tkinter GUI.

[https://github.com/yusufKh7-ctrl/File_organizer](https://github.com/yusufKh7-ctrl/File_organizer)

## Features

- Modern and intuitive graphical user interface
- Choose **any folder** to organize (not limited to Downloads)
- **Preview mode** (dry-run) — see exactly what will happen before moving anything
- Intelligent duplicate file handling (automatically renames when needed)
- Safe operation — skips locked / in-use files
- Cross-category file sorting with customizable selection
- Windows executable available (one-file .exe)

## Supported File Categories

| Folder         | Common Extensions                                                               |
|----------------|---------------------------------------------------------------------------------|
| Images        | jpg, jpeg, png, gif, webp, svg, heic, bmp, tiff, ico                             |
| Videos        | mp4, mkv, webm, avi, mov, wmv, flv, mpeg, 3gp, m4v                               |
| Documents     | pdf, doc, docx, txt, md, csv, xlsx, pptx, odt, rtf, epub                         |
| Audio         | mp3, wav, flac, m4a, ogg, aac, wma, opus                                         |
| Archives      | zip, rar, 7z, tar, gz, bz2, xz, iso                                              |
| Applications  | exe, msi, dmg, apk, deb, rpm, jar                                                |
| Others        | everything else                                                                  |

## Screenshots

<img width="846" height="1057" alt="Screenshot 2026-01-22 112021" src="https://github.com/user-attachments/assets/4e9e4a67-5b7c-4801-8c71-451874b93c3c" />

## Download Standalone Executable (Windows)

Go to → [Releases](https://github.com/yusufKh7-ctrl/File_organizer/releases)  
Download the latest `File_Organizer.exe`

## Quick Start (from source)

```bash
# 1. Clone the repository
git clone https://github.com/yusufKh7-ctrl/File_organizer.git
cd File_organizer

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 3. Install requirements (usually only needed for future extensions)
pip install -r requirements.txt

# 4. Run the application
python src/main.py
# or directly
python src/gui.py

# Download Standalone Executable (Windows)
Go to → Releases
Download the latest File_Organizer.exe

# Building the executable yourself
### Make sure you're in the virtual environment
pip install pyinstaller

### Recommended way (using the provided spec file)
pyinstaller File_Organizer.spec

### Alternative one-liner
pyinstaller --onefile --windowed --icon=assets/robot.ico src/gui.py

## The executable will appear in the dist/ folder.


```
### **Made with ❤️ and Python**
