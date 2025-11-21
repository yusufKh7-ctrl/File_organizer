from pathlib import Path


DOWNLOADS_PATH = Path.home() / 'Downloads'

EXTENSION_TO_FOLDER = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg", ".tiff"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v"},
    "Applications": {".exe", ".msi", ".deb", ".dmg", ".apk", ".app"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".pptx", ".csv", ".rtf"},
    "Audio": {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"},
}

FOLDERS = ['Images', 'Videos', 'Applications', 'Archives', 'Documents', 'Audio', 'Others']
