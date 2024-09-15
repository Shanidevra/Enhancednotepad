import tkinter as tk
from tkinter import filedialog, messagebox, font

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt",
                                      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, "r") as f:
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, f.read())

def save_file():
    file = filedialog.asksaveasfilename(initialfile="untitled.txt",
                                        defaultextension=".txt",
                                        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, tk.END))
            messagebox.showinfo("File Saved", "File has been saved successfully!")

def quit_app():
    root.quit()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def change_font(font_family):
    current_font = font.Font(font=text_area['font'])
    current_font.config(family=font_family)
    text_area.config(font=current_font)

def toggle_wrap():
    if text_area.cget("wrap") == "none":
        text_area.config(wrap="word")
    else:
        text_area.config(wrap="none")

def show_about():
    messagebox.showinfo("About", "Simple Notepad\nVersion 1.0\nCreated using Python and Tkinter.")

root = tk.Tk()
root.title("Enhanced Notepad")

text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Format Menu
format_menu = tk.Menu(menu_bar, tearoff=0)
font_menu = tk.Menu(format_menu, tearoff=0)
font_menu.add_command(label="Arial", command=lambda: change_font("Arial"))
font_menu.add_command(label="Courier", command=lambda: change_font("Courier"))
font_menu.add_command(label="Times New Roman", command=lambda: change_font("Times New Roman"))
format_menu.add_cascade(label="Font", menu=font_menu)
format_menu.add_command(label="Word Wrap", command=toggle_wrap)
menu_bar.add_cascade(label="Format", menu=format_menu)

# View Menu
view_menu = tk.Menu(menu_bar, tearoff=0)
# Additional view options can be added here
menu_bar.add_cascade(label="View", menu=view_menu)

# Help Menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

root.mainloop()
