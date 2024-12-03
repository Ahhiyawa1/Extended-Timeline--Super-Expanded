import re
from tkinter import Tk, filedialog

def adjust_dates_in_file(filepath):
    """Adjusts the dates in the EU4 script file by adding 2098 years."""
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Regex to match date-related fields
    date_pattern = re.compile(r'(is_year|year|date)\s*=\s*(\d+)')
    
    adjusted_lines = []
    for line in lines:
        match = date_pattern.search(line)
        if match:
            field, year = match.groups()
            new_year = int(year) + 2098
            adjusted_line = date_pattern.sub(f"{field} = {new_year}", line)
            adjusted_lines.append(adjusted_line)
        else:
            adjusted_lines.append(line)
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.writelines(adjusted_lines)
    print(f"Updated dates in {filepath}")

def main():
    """Main function to select file and adjust dates."""
    Tk().withdraw()  # Hide the root window
    filepath = filedialog.askopenfilename(
        title="Select an EU4 script file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    
    if not filepath:
        print("No file selected. Exiting.")
        return
    
    adjust_dates_in_file(filepath)
    print("Date adjustment complete.")

if __name__ == "__main__":
    main()
