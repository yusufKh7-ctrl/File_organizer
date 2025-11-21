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
        
        
        #Retrieve the files located inside the 'Downloads' folder
        for file in self.downloads_path.iterdir():
            if not file.is_file():
                continue
            
            extension = file.suffix.lower()
        
            target_folder = 'Others'
            for folder_name, extensions in self.extension_to_folder.items():
                if extension in extensions:
                    target_folder = folder_name
                    break
            destination = self.downloads_path / target_folder / file.name
            
            try:
                shutil.move(str(file), str(destination))
                self.moved_count += 1
                print(f'{file.name} → {target_folder}')
            except (PermissionError, shutil.Error):
                print('the {file.name} was not transferred')
            
        print(f'{self.moved_count} files were successfully tranferred!')