import customtkinter as ctk
from tkinter import filedialog, messagebox
from pathlib import Path
import os

# --- PRE-DEFINITION TO AVOID UNBOUND ERRORS ---
# Setting default values to ensure variables are always defined
FOLDERS = ["Images", "Videos", "Documents", "Others"]
EXTENSION_TO_FOLDER = {}
OrganizerFiles = None

# --- SECURE IMPORT BLOCK ---
try:
    from config import FOLDERS as CFG_FOLDERS, EXTENSION_TO_FOLDER as CFG_EXT
    from organizer import OrganizerFiles as OrgClass
    
    FOLDERS = CFG_FOLDERS
    EXTENSION_TO_FOLDER = CFG_EXT
    OrganizerFiles = OrgClass
except ImportError:
    # Fallback to defaults if external files are missing
    EXTENSION_TO_FOLDER = {".jpg": "Images", ".mp4": "Videos", ".pdf": "Documents"}
    print("Warning: config.py or organizer.py not found. Running with defaults.")

class FileOrganizer(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Configuration ---
        self.title("File Organizer Professional Edition")
        self.geometry("1000x700")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Color Palette
        self.accent_color = "#3B8ED0"
        self.success_color = "#2ecc71"

        # Grid Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_main_content()

    def create_sidebar(self):
        """Creates the navigation sidebar and theme settings."""
        self.sidebar = ctk.CTkFrame(self, width=240, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text="📁 PRO\nORGANIZER", 
                                     font=ctk.CTkFont(size=26, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(40, 30))

        # Status Indicator
        self.stat_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.stat_frame.grid(row=1, column=0, padx=20, pady=20)
        
        self.status_indicator = ctk.CTkLabel(self.stat_frame, text="● System Ready", 
                                            text_color=self.success_color, font=ctk.CTkFont(size=12))
        self.status_indicator.pack()

        # Appearance Settings
        self.appearance_label = ctk.CTkLabel(self.sidebar, text="Appearance Mode:", anchor="w")
        self.appearance_label.grid(row=5, column=0, padx=20, pady=(10, 0), sticky="s")
        self.appearance_menu = ctk.CTkOptionMenu(self.sidebar, values=["Light", "Dark", "System"],
                                                 command=lambda m: ctk.set_appearance_mode(m))
        self.appearance_menu.grid(row=6, column=0, padx=20, pady=(10, 30))
        self.sidebar.grid_rowconfigure(4, weight=1)

    def create_main_content(self):
        """Creates the main workspace with path selection and categories."""
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=40, pady=40, sticky="nsew")

        # 1. Directory Card
        self.path_card = ctk.CTkFrame(self.main_frame, border_width=1, border_color="#ADB5BD")
        self.path_card.pack(fill="x", pady=(0, 25), ipady=15)
        
        ctk.CTkLabel(self.path_card, text="📍 Source Directory", font=ctk.CTkFont(size=15, weight="bold")).pack(pady=(10, 5), padx=20, anchor="w")
        
        self.path_var = ctk.StringVar()
        container = ctk.CTkFrame(self.path_card, fg_color="transparent")
        container.pack(fill="x", padx=20)

        self.entry_path = ctk.CTkEntry(container, textvariable=self.path_var, placeholder_text="Path to clean up...", height=45)
        self.entry_path.pack(side="left", padx=(0, 10), expand=True, fill="x")
        
        self.btn_browse = ctk.CTkButton(container, text="Select Folder", width=120, height=45, 
                                        font=ctk.CTkFont(weight="bold"), command=self.browse_folder)
        self.btn_browse.pack(side="right")

        # 2. Categories List
        self.cat_frame = ctk.CTkScrollableFrame(self.main_frame, label_text="Categories to Include", 
                                                label_font=ctk.CTkFont(size=15, weight="bold"), border_width=1)
        self.cat_frame.pack(fill="both", expand=True, pady=10)

        self.check_vars = {}
        for folder in FOLDERS:
            var = ctk.BooleanVar(value=True)
            self.check_vars[folder] = var
            cb = ctk.CTkCheckBox(self.cat_frame, text=f"  {folder}", variable=var, 
                                 checkbox_width=22, checkbox_height=22, font=ctk.CTkFont(size=14))
            cb.pack(pady=10, padx=25, anchor="w")

        # 3. Action Buttons
        self.action_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.action_frame.pack(fill="x", pady=(30, 0))

        self.btn_preview = ctk.CTkButton(self.action_frame, text="🔍 Preview Changes", 
                                         height=55, fg_color="transparent", border_width=2,
                                         border_color=self.accent_color, text_color=(self.accent_color, "white"),
                                         hover_color=("#E9ECEF", "#343A40"), command=self.show_preview)
        self.btn_preview.grid(row=0, column=0, padx=(0, 10), sticky="ew")

        self.btn_run = ctk.CTkButton(self.action_frame, text="🚀 Organize Files", 
                                     fg_color=self.success_color, hover_color="#27ae60",
                                     text_color="white", height=55, font=ctk.CTkFont(size=18, weight="bold"),
                                     command=self.start_organizing)
        self.btn_run.grid(row=0, column=1, padx=(10, 0), sticky="ew")
        
        self.action_frame.grid_columnconfigure((0, 1), weight=1)

    # --- Core Logic Functions ---

    def browse_folder(self):
        path = filedialog.askdirectory()
        if path: self.path_var.set(path)

    def start_organizing(self):
        """Triggers the actual file movement and shows a report."""
        path = self.path_var.get().strip()
        
        # Check if the core organizer class was imported successfully
        if OrganizerFiles is None:
            messagebox.showerror("Error", "Organizer core module missing!")
            return

        if not path or not Path(path).exists():
            messagebox.showerror("Error", "Please select a valid folder first.")
            return

        selected = [f for f, v in self.check_vars.items() if v.get()]
        
        try:
            org = OrganizerFiles()
            org.set_path(path)
            org.target_folders = selected
            
            # Tracking moved files for the final report
            moved_files = []
            for file in Path(path).iterdir():
                if file.is_file():
                    ext = file.suffix.lower()
                    for folder, exts in EXTENSION_TO_FOLDER.items():
                        if ext in exts and folder in selected:
                            moved_files.append(f"• {file.name} ➔ {folder}")
                            break
            
            org.run() # Execute organization
            self.show_completion_report(len(moved_files), moved_files, path)

        except Exception as e:
            messagebox.showerror("Process Error", str(e))

    def show_preview(self):
        """Simulates file movement without making changes."""
        path = self.path_var.get().strip()
        if not path or not Path(path).exists():
            messagebox.showerror("Selection Required", "Select a folder to see the preview.")
            return

        preview_win = ctk.CTkToplevel(self)
        preview_win.title("Preview - Dry Run")
        preview_win.geometry("750x550")
        preview_win.after(100, lambda: preview_win.focus())

        txt = ctk.CTkTextbox(preview_win, width=700, height=450, font=("Consolas", 12))
        txt.pack(padx=20, pady=20, fill="both", expand=True)

        log = [f"SCANNING: {path}\n", "="*50]
        selected = [f for f, v in self.check_vars.items() if v.get()]
        
        for file in Path(path).iterdir():
            if file.is_file():
                found = False
                for folder, exts in EXTENSION_TO_FOLDER.items():
                    if file.suffix.lower() in exts and folder in selected:
                        log.append(f"[WILL MOVE] {file.name} -> {folder}")
                        found = True
                        break
                if not found: log.append(f"[STAYING]  {file.name}")

        txt.insert("0.0", "\n".join(log))
        txt.configure(state="disabled")

    def show_completion_report(self, count, log, target_path):
        """Opens a summary window after a successful operation."""
        report = ctk.CTkToplevel(self)
        report.title("Organization Complete")
        report.geometry("650x500")
        report.after(100, lambda: report.focus())

        ctk.CTkLabel(report, text="✅ Mission Accomplished!", font=ctk.CTkFont(size=20, weight="bold"), text_color=self.success_color).pack(pady=20)
        ctk.CTkLabel(report, text=f"Total Files Organized: {count}").pack()

        log_box = ctk.CTkTextbox(report, width=600, height=250)
        log_box.pack(padx=20, pady=15, fill="both", expand=True)
        log_box.insert("0.0", "\n".join(log) if log else "Everything was already in order!")
        log_box.configure(state="disabled")

        btn_frame = ctk.CTkFrame(report, fg_color="transparent")
        btn_frame.pack(pady=20)

        # Button to open the organized folder in File Explorer
        ctk.CTkButton(btn_frame, text="Open Folder", fg_color="#34495e", command=lambda: os.startfile(target_path)).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Close", command=report.destroy).pack(side="right", padx=10)

if __name__ == "__main__":
    app = FileOrganizer()
    app.mainloop()