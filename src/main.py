import sys
import argparse
import customtkinter as ctk
from gui import FileOrganizer

# Try to import CustomTkinter and the GUI class
try:
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False

def run_cli(args):
    """
    Handles the Command Line Interface logic.
    Executes organization without opening a window.
    """
    try:
        from organizer import OrganizerFiles
        
        org = OrganizerFiles()
        
        # Override path if provided in arguments
        if args.path:
            org.set_path(args.path)
            
        print(f"🚀 Starting organization in: {org.path}")
        print(f"🛠️  Mode: {'Dry Run' if args.dry_run or args.preview else 'Live Execution'}")
        print("-" * 50)
        
        # Execute the core logic
        org.run(dry_run=args.dry_run, preview_only=args.preview)
        
        print("-" * 50)
        print("✅ Success: Operation completed.")
        return 0
        
    except Exception as e:
        print(f"❌ Critical Error: {e}")
        return 1

def run_gui():
    """
    Initializes and starts the modern Graphical User Interface.
    """
    if not GUI_AVAILABLE:
        print("⚠️  Error: customtkinter library not found.")
        print("💡 Action: Run 'pip install customtkinter' to use GUI mode.")
        return 1 

    # Initialize the high-end UI
    app = FileOrganizer()
    app.mainloop()
    return 0

if __name__ == "__main__":
    # Setup Argument Parser for CLI support
    parser = argparse.ArgumentParser(
        description="File Organizer Pro - Automate your directory management."
    )
    
    parser.add_argument("path", nargs="?", help="Directory path to organize.")
    parser.add_argument("--cli", action="store_true", help="Force Command Line Interface mode.")
    parser.add_argument("--dry-run", action="store_true", help="Simulate execution without moving files.")
    parser.add_argument("--preview", action="store_true", help="Display a summary of changes.")

    args = parser.parse_args()

    # Intelligent mode selection:
    # Use CLI if explicitly requested, if specific flags are passed, or if GUI libs are missing.
    if args.cli or (args.path and (args.dry_run or args.preview)) or not GUI_AVAILABLE:
        sys.exit(run_cli(args))
    else:
        sys.exit(run_gui())