import sys
from pathlib import Path
import argparse

try:
    import tkinter as tk
    from gui import FileOrganizerGUI
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False


def run_cli(args):
    from organizer import OrganizerFiles

    org = OrganizerFiles()
    
    if args.path:
        try:
            org.set_path(args.path)
        except ValueError as e:
            print(e)
            return 1

    print(f"Target folder: {org.path}")
    print("Dry run mode:", "ON" if args.dry_run else "OFF")
    
    org.organize(dry_run=args.dry_run, preview_only=args.preview)
    return 0


def run_gui():
    if not TKINTER_AVAILABLE:
        print("Tkinter is not available. Cannot run GUI mode.")
        return 1

    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Organizer")
    parser.add_argument("path", nargs="?", help="Folder to organize (default: ~/Downloads)")
    parser.add_argument("--cli", action="store_true", help="Force CLI mode")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without moving files")
    parser.add_argument("--preview", action="store_true", help="Only show what would happen")

    args = parser.parse_args()

    if args.cli or not TKINTER_AVAILABLE:
        sys.exit(run_cli(args))
    else:
        sys.exit(run_gui())