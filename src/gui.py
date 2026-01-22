import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, Toplevel
from pathlib import Path
from config import FOLDERS, EXTENSION_TO_FOLDER
from organizer import OrganizerFiles

class FileOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("680x820")
        self.root.config(bg="#F5F7FA")
        self.root.resizable(False, False)

        # Colors
        self.COLOR_BG = "#F5F7FA"
        self.COLOR_PRIMARY = "#4361EE"
        self.COLOR_SUCCESS = "#06D6A0"
        self.COLOR_PREVIEW = "#FFB703"
        self.COLOR_TEXT = "#2D3436"
        self.COLOR_LIGHT = "#FFFFFF"
        self.COLOR_BORDER = "#DEE2E6"

        # Fonts
        self.font_title = ("Segoe UI", 20, "bold")
        self.font_section = ("Segoe UI", 11, "bold")
        self.font_normal = ("Segoe UI", 10)
        self.font_footer = ("Segoe UI", 9)

        # Title
        self.create_header()

        # Main content
        main_container = tk.Frame(root, bg=self.COLOR_BG)
        main_container.pack(fill="both", expand=True, padx=35, pady=(10, 20))

        self.create_path_section(main_container)
        self.create_folders_section(main_container)
        self.create_buttons(main_container)

        # Footer
        self.create_footer()

    def create_header(self):
        header = tk.Frame(self.root, bg=self.COLOR_BG)
        header.pack(pady=(30, 20))

        tk.Label(
            header,
            text="Automatic File Organizer",
            bg=self.COLOR_BG,
            fg=self.COLOR_PRIMARY,
            font=self.font_title
        ).pack()

        tk.Label(
            header,
            text="Sort your files into folders by type — instantly",
            bg=self.COLOR_BG,
            fg="#636E72",
            font=("Segoe UI", 10)
        ).pack(pady=(6, 0))

    def create_path_section(self, parent):
        frame = tk.LabelFrame(
            parent,
            text=" Select Folder to Organize",
            font=self.font_section,
            bg=self.COLOR_LIGHT,
            fg=self.COLOR_TEXT,
            relief="flat",
            bd=1,
            highlightbackground=self.COLOR_BORDER,
            highlightthickness=1,
            padx=20, pady=20
        )
        frame.pack(fill="x", pady=(0, 20))

        row = tk.Frame(frame, bg=self.COLOR_LIGHT)
        row.pack(fill="x", pady=5)

        self.path_var = tk.StringVar()
        self.path_entry = tk.Entry(
            row,
            textvariable=self.path_var,
            font=self.font_normal,
            bg="white",
            relief="flat",
            highlightthickness=2,
            highlightbackground=self.COLOR_BORDER,
            highlightcolor=self.COLOR_PRIMARY,
            insertwidth=1
        )
        self.path_entry.pack(side="left", fill="x", expand=True, ipady=10)

        browse_btn = tk.Button(
            row, text="Browse", command=self.browse_folder,
            bg=self.COLOR_PRIMARY, fg="white", font=self.font_normal,
            relief="flat", cursor="hand2", width=12
        )
        browse_btn.pack(side="right", padx=(10, 0))
        self.style_button_hover(browse_btn, self.COLOR_PRIMARY, "#3651D4")

    def create_folders_section(self, parent):
        frame = tk.LabelFrame(
            parent,
            text=" Organize Files Into These Folders",
            font=self.font_section,
            bg=self.COLOR_LIGHT,
            fg=self.COLOR_TEXT,
            relief="flat",
            bd=1,
            highlightbackground=self.COLOR_BORDER,
            highlightthickness=1,
            padx=20, pady=15
        )
        frame.pack(fill="both", expand=True, pady=(0, 25))

        self.check_vars = {}
        for i, folder in enumerate(FOLDERS):
            var = tk.BooleanVar(value=True)
            self.check_vars[folder] = var

            row = tk.Frame(frame, bg=self.COLOR_LIGHT)
            row.pack(fill="x", pady=4)

            cb = tk.Checkbutton(
                row, variable=var, bg=self.COLOR_LIGHT, fg=self.COLOR_TEXT,
                selectcolor=self.COLOR_PRIMARY, activebackground=self.COLOR_LIGHT,
                font=self.font_normal, cursor="hand2"
            )
            cb.pack(side="left", padx=(5, 0))

            tk.Label(
                row, text=folder, bg=self.COLOR_LIGHT, fg=self.COLOR_TEXT,
                font=self.font_normal, anchor="w"
            ).pack(side="left", padx=(8, 0), fill="x", expand=True)

            if i < len(FOLDERS) - 1:
                sep = tk.Frame(frame, height=1, bg=self.COLOR_BORDER)
                sep.pack(fill="x", padx=10)

    def create_buttons(self, parent):
        btn_frame = tk.Frame(parent, bg=self.COLOR_BG)
        btn_frame.pack(pady=20)

        start_btn = tk.Button(
            btn_frame,
            text="Start Organizing Now",
            command=self.start_organizing,
            bg=self.COLOR_SUCCESS,
            fg="white",
            font=("Segoe UI", 13, "bold"),
            relief="flat",
            cursor="hand2",
            height=2,
            width=25
        )
        start_btn.grid(row=0, column=0, padx=10)
        self.style_button_hover(start_btn, self.COLOR_SUCCESS, "#05BF8A")

        preview_btn = tk.Button(
            btn_frame,
            text="Preview Changes Only",
            command=self.show_preview_window,
            bg=self.COLOR_PREVIEW,
            fg="black",
            font=("Segoe UI", 13, "bold"),
            relief="flat",
            cursor="hand2",
            height=2,
            width=25
        )
        preview_btn.grid(row=0, column=1, padx=10)
        self.style_button_hover(preview_btn, self.COLOR_PREVIEW, "#FFC107")

    def create_footer(self):
        footer_frame = tk.Frame(self.root, bg=self.COLOR_BG)
        footer_frame.pack(side="bottom", fill="x", pady=(15, 20))

        tk.Label(
            footer_frame,
            text="Made with Python • Organized Life, Organized Mind",
            font=self.font_footer,
            bg=self.COLOR_BG,
            fg="#95A5A6"
        ).pack()

    def style_button_hover(self, button, color_on_enter, color_on_leave):
        def on_enter(e): button.config(bg=color_on_enter)
        def on_leave(e): button.config(bg=color_on_leave)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.path_var.set(folder_path)

    def get_selected_folders(self):
        return [f for f, v in self.check_vars.items() if v.get()]

    def start_organizing(self):
        path = self.path_var.get().strip()
        if not path:
            messagebox.showerror("Error", "Please select a folder first.")
            return

        selected = self.get_selected_folders()
        if not selected:
            messagebox.showerror("Error", "Please select at least one folder.")
            return

        try:
            organizer = OrganizerFiles()
            organizer.downloads_path = Path(path)
            organizer.folders = selected
            organizer.run()  

            messagebox.showinfo(
                "Success ✓",
                f"{organizer.moved_count} files organized successfully!\n"
                "Your folder is now clean and tidy."
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_preview_window(self):
        path = self.path_var.get().strip()
        if not path:
            messagebox.showerror("Error", "Please select a folder first.")
            return

        selected = self.get_selected_folders()
        if not selected:
            messagebox.showerror("Error", "Please select at least one folder.")
            return

        preview_window = Toplevel(self.root)
        preview_window.title("Preview - No files will be moved")
        preview_window.geometry("700x500")
        preview_window.configure(bg="#F5F7FA")
        preview_window.transient(self.root)
        preview_window.grab_set()

        tk.Label(
            preview_window,
            text="Preview of changes (dry-run)",
            font=("Segoe UI", 14, "bold"),
            bg="#F5F7FA",
            fg="#4361EE"
        ).pack(pady=10)

        text_area = scrolledtext.ScrolledText(
            preview_window,
            wrap=tk.WORD,
            width=80,
            height=22,
            font=("Consolas", 10),
            bg="#FFFFFF",
            fg="#2D3436"
        )
        text_area.pack(padx=15, pady=10, fill="both", expand=True)

        # Organizational simulation
        lines = []
        lines.append(f"Folder: {path}")
        lines.append("-" * 70)

        moved = 0
        try:
            for file in Path(path).iterdir():
                if not file.is_file():
                    continue

                ext = file.suffix.lower()
                target = "Others"
                for folder_name, exts in EXTENSION_TO_FOLDER.items():
                    if ext in exts and folder_name in selected:
                        target = folder_name
                        break

                dest = Path(path) / target / file.name
                note = ""
                if dest.exists():
                    note = " (will be renamed to avoid conflict)"

                lines.append(f"{file.name:<45}  →  {target}/{file.name}{note}")
                moved += 1

            lines.append("-" * 70)
            lines.append(f"Total files that would be moved: {moved}")
            lines.append("Nothing has been changed — this is just a preview.")

        except Exception as e:
            lines.append(f"Error during preview: {str(e)}")

        text_area.insert(tk.END, "\n".join(lines))
        text_area.config(state="disabled")

        tk.Button(
            preview_window,
            text="Close",
            command=preview_window.destroy,
            bg="#4361EE",
            fg="white",
            font=("Segoe UI", 11),
            width=12
        ).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()