import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re

def add_years(year, offset=2098):
    return str(int(year) + offset)

def modify_dates(content):
    # Modify 'is_year = ', 'year =' and 'date =' lines by adding 2098 to the year component
    content = re.sub(r'(is_year\s*=\s*)(\d+)', lambda m: m.group(1) + add_years(m.group(2)), content)
    content = re.sub(r'(year\s*=\s*)(\d+)', lambda m: m.group(1) + add_years(m.group(2)), content)
    content = re.sub(r'(date\s*=\s*)(\d+)\.(\d+)\.(\d+)', 
                     lambda m: m.group(1) + add_years(m.group(2)) + f'.{m.group(3)}.{m.group(4)}', 
                     content)
    return content

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    modified_content = modify_dates(content)
    return modified_content

def save_output(content, output_path):
    with open(output_path, 'w') as file:
        file.write(content)

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        modified_content = process_file(file_path)
        show_output_dialog(modified_content, file_path)

def browse_directory():
    dir_path = filedialog.askdirectory()
    if dir_path:
        for filename in os.listdir(dir_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(dir_path, filename)
                modified_content = process_file(file_path)
                output_path = os.path.join(dir_path, f"modified_{filename}")
                save_output(modified_content, output_path)
        messagebox.showinfo("Process Complete", "All files in the directory have been processed and saved.")

def show_output_dialog(modified_content, file_path):
    output_window = tk.Toplevel(root)
    output_window.title("Modified Content")
    output_text = tk.Text(output_window, wrap="word")
    output_text.insert("1.0", modified_content)
    output_text.pack(expand=True, fill="both")

    save_button = tk.Button(output_window, text="Save", 
                            command=lambda: save_output(modified_content, f"modified_{os.path.basename(file_path)}"))
    save_button.pack()

# GUI setup
root = tk.Tk()
root.title("EU4 Date Modifier")

instruction = tk.Label(root, text="Select a text file or directory to adjust dates:")
instruction.pack(pady=5)

file_button = tk.Button(root, text="Select File", command=browse_file)
file_button.pack(pady=5)

directory_button = tk.Button(root, text="Select Directory", command=browse_directory)
directory_button.pack(pady=5)

root.mainloop()
