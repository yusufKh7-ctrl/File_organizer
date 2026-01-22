from pathlib import Path
import shutil
import logging
from typing import Optional

from config import EXTENSION_TO_FOLDER, FOLDERS, IGNORED_FOLDERS

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    datefmt="%H:%M:%S"
)


class OrganizerFiles:
    def __init__(self):
        self.path: Path = Path.home() / "Downloads"
        self.extension_map = EXTENSION_TO_FOLDER
        self.target_folders = FOLDERS
        self.moved_count = 0
        self.skipped_count = 0
        self.ignored_count = 0

    def set_path(self, path: str | Path) -> None:
        """Set the folder to organize"""
        p = Path(path).expanduser().resolve()
        if not p.exists() or not p.is_dir():
            raise ValueError(f"Not a valid directory: {p}")
        self.path = p

    def get_category(self, ext: str) -> str:
        ext = ext.lower()
        for category, extensions in self.extension_map.items():
            if ext in extensions:
                return category
        return "Others"

    def should_skip(self, item: Path) -> bool:
        if item.is_dir():
            return item.name in IGNORED_FOLDERS or item.name.startswith(".")
        return False

    def organize(self, dry_run: bool = False, preview_only: bool = False) -> None:
        """
        Main organizing function
        dry_run     → simulate without moving
        preview_only → only print what would happen (no folder creation either)
        """
        if not self.path.exists():
            logging.error(f"Directory does not exist: {self.path}")
            return

        logging.info(f"Organizing folder: {self.path}")

        # Create target folders (unless preview_only)
        if not preview_only and not dry_run:
            for folder in self.target_folders:
                (self.path / folder).mkdir(exist_ok=True)

        for item in self.path.iterdir():
            if self.should_skip(item):
                self.ignored_count += 1
                continue

            if not item.is_file():
                continue

            ext = item.suffix
            category = self.get_category(ext)
            destination_dir = self.path / category

            # Handle name conflicts
            dest_path = destination_dir / item.name
            counter = 1
            while dest_path.exists():
                stem, suffix = item.stem, item.suffix
                dest_path = destination_dir / f"{stem} ({counter}){suffix}"
                counter += 1

            action = "Would move" if dry_run or preview_only else "Moving"
            logging.info(f"{action}: {item.name:.<50} → {category}/{dest_path.name}")

            if dry_run or preview_only:
                self.moved_count += 1  # count simulation
                continue

            try:
                shutil.move(item, dest_path)
                self.moved_count += 1
            except (PermissionError, shutil.Error) as e:
                logging.warning(f"Skipped {item.name}: {e}")
                self.skipped_count += 1

        logging.info("-" * 60)
        logging.info(f"Finished → Moved: {self.moved_count} | Skipped: {self.skipped_count} | Ignored: {self.ignored_count}")