# Downloads File Organizer 🗃️

A clean, object-oriented Python script that automatically organizes your Downloads folder by file type.

## Features
- Automatically sorts files into: Images, Videos, Documents, Audio, Archives, Applications, Others
- Cross-platform (Windows, macOS, Linux) using `Path.home()`
- Safe moving (skips open/in-use files)
- Real-time progress printing
- Uses modern Python practices (pathlib, OOP, virtual environments)

## How to Use
```bash
git clone https://github.com/yusufKh7-ctrl/File_organizer.git
cd File_organizer
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate   # macOS/Linux
python src/main.py