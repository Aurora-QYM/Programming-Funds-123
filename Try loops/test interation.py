import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    pass

import tkinter as tk
from tkinter import ttk, messagebox

class MinimalEnglishApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Management Platform")
        self.geometry("900x600")
        self.configure(bg="#f8f9fa")  # 极浅灰背景，简约风

        # ========== 全局样式配置（核心美化部分） ==========
        style = ttk.Style(self)
        # 选择主题：vista / clam / alt / default；clam最适合自定义简约风格
        style.theme_use("clam")

        # 定义全局字体常量
        FONT_TITLE = ("Segoe UI", 16)
        FONT_TEXT = ("Segoe UI", 11)
        FONT_BTN = ("Segoe UI", 11)

        # 标签样式
        style.configure("TLabel",
                        font=FONT_TEXT,
                        background="#f8f9fa",
                        foreground="#212529")
        # 按钮样式：扁平化、去掉3D凸起，简约大气
        style.configure("TButton",
                        font=FONT_BTN,
                        padding=(12, 4),
                        relief="flat",  # 扁平化，无凸起边框
                        background="#e9ecef")
        style.map("TButton",
                  background=[("active", "#dee2e6")]) # hover悬浮变色
        # 输入框
        style.configure("TEntry",
                        font=FONT_TEXT,
                        padding=4)
        # 框架容器
        style.configure("TFrame", background="#f8f9fa")

        # ========== 菜单（英文菜单） ==========
        menubar = tk.Menu(self)
        menu_file = tk.Menu(menubar, tearoff=0)
        menu_file.add_command(label="Open", command=self.dummy)
        menu_file.add_command(label="Save", command=self.dummy)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=menu_file)

        menu_help = tk.Menu(menubar, tearoff=0)
        menu_help.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=menu_help)
        self.config(menu=menubar)

        # ========== 页面内容 ==========
        main_frame = ttk.Frame(self, padding=40)
        main_frame.pack(fill="both", expand=True)

        ttk.Label(main_frame, text="Management Dashboard", font=FONT_TITLE).pack(anchor="w")
        ttk.Separator(main_frame, orient="horizontal").pack(fill="x", pady=12)

        ttk.Label(main_frame, text="Welcome to the system dashboard.", font=FONT_TEXT).pack(anchor="w", pady=6)
        ttk.Button(main_frame, text="New Task").pack(anchor="w", pady=10)

    def dummy(self):
        pass
    def show_about(self):
        messagebox.showinfo("About", "Minimal Platform v1.0")

if __name__ == "__main__":
    app = MinimalEnglishApp()
    app.mainloop()
