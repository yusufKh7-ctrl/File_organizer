from config import DOWNLOADS_PATH, EXTENSION_TO_FOLDER, FOLDERS
from pathlib import Path
import shutil


class DownloadsOrganizer:
    def __init__(self):
        self.downloads_path = DOWNLOADS_PATH
        self.extension_to_folder = EXTENSION_TO_FOLDER
        self.folders = FOLDERS
        self.moved_count = 0
        
    def run(self):
        #check if 'Downloads' folder exists or not
        if not self.downloads_path.exists():
            print('Downloads folder was not found.')
            return
        #Creating new folders
        for folders in self.folders:
                folder_path = self.downloads_path / folders
                folder_path.mkdir(exist_ok=True)
        
        print('Files are being sorted...')
        print(f'{self.moved_count} files were successfully tranferred!.')
        
    
