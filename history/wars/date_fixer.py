import os
import re
from tkinter import Tk, filedialog

def read_file_with_fallback(filepath):
    """Reads a file with multiple fallback encodings."""
    encodings = ['utf-8', 'cp1252', 'latin1']
    for encoding in encodings:
        try:
            with open(filepath, 'r', encoding=encoding) as file:
                return file.readlines()
        except UnicodeDecodeError:
            continue
    # Final fallback with 'replace' to ensure the file is read
    with open(filepath, 'r', encoding='utf-8', errors='replace') as file:
        return file.readlines()

def adjust_dates_in_file(filepath):
    """Adjusts the dates in the EU4 script file by adding 2098 years."""
    lines = read_file_with_fallback(filepath)
    
    # Regex to match date-related fields or standard EU4 date format
    date_pattern = re.compile(r'(is_year|year|date)\s*=\s*(\d+)|\b(\d{1,4}\.\d{1,2}\.\d{1,2})\b')
    
    adjusted_lines = []
    for line in lines:
        def replace_date(match):
            if match.group(3):  # Matches standard date format YYYY.MM.DD
                parts = match.group(3).split('.')
                parts[0] = str(int(parts[0]) + 2098)  # Adjust year
                return '.'.join(parts)
            else:
                field, year = match.groups()[:2]
                new_year = int(year) + 2098
                return f"{field} = {new_year}"
        
        adjusted_line = date_pattern.sub(replace_date, line)
        adjusted_lines.append(adjusted_line)
    
    # Write back to file, replacing unencodable characters if needed
    try:
        with open(filepath, 'w', encoding='cp1252', errors='replace') as file:
            file.writelines(adjusted_lines)
        print(f"Updated dates in {filepath}")
    except UnicodeEncodeError as e:
        print(f"Failed to write file {filepath} due to encoding error: {e}")
        print("Switching to UTF-8 encoding.")
        with open(filepath, 'w', encoding='utf-8', errors='replace') as file:
            file.writelines(adjusted_lines)
        print(f"File {filepath} written with UTF-8 instead.")

def process_directory(directory):
    """Processes all .txt files in a directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                filepath = os.path.join(root, file)
                adjust_dates_in_file(filepath)
    print(f"Processed all .txt files in {directory}")

def main():
    """Main function to select file or directory and adjust dates."""
    Tk().withdraw()  # Hide the root window
    choice = input("Do you want to process a file or a directory? (file/dir): ").strip().lower()
    
    if choice == 'file':
        filepath = filedialog.askopenfilename(
            title="Select an EU4 script file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not filepath:
            print("No file selected. Exiting.")
            return
        adjust_dates_in_file(filepath)
    elif choice == 'dir':
        directory = filedialog.askdirectory(title="Select a directory containing EU4 script files")
        if not directory:
            print("No directory selected. Exiting.")
            return
        process_directory(directory)
    else:
        print("Invalid choice. Exiting.")
        return

    print("Date adjustment complete.")

if __name__ == "__main__":
    main()
