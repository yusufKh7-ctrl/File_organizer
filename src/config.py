"""
Configuration for file organizer categories and extensions
"""

FOLDERS = [
    "Images",
    "Videos",
    "Documents",
    "Audio",
    "Archives",
    "Applications",
    "Others"
]

EXTENSION_TO_FOLDER = {
    # Images
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".tiff", ".tif", ".heic", ".ico"
    ],
    # Videos
    "Videos": [
        ".mp4", ".mkv", ".webm", ".avi", ".mov", ".wmv", ".flv", ".mpeg", ".mpg", ".3gp", ".m4v"
    ],
    # Documents
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".md", ".markdown", ".csv", ".xlsx", ".xls",
        ".ppt", ".pptx", ".pages", ".epub", ".mobi"
    ],
    # Audio
    "Audio": [
        ".mp3", ".wav", ".flac", ".m4a", ".ogg", ".aac", ".wma", ".opus", ".aiff", ".alac"
    ],
    # Archives / Compressed
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".cab"
    ],
    # Executables / Installers
    "Applications": [
        ".exe", ".msi", ".dmg", ".apk", ".deb", ".rpm", ".appx", ".jar"
    ],
    # You can add more categories later if needed
}

# Optional: folders that should be ignored / not scanned
IGNORED_FOLDERS = {"$RECYCLE.BIN", "System Volume Information", ".git", "__pycache__"}