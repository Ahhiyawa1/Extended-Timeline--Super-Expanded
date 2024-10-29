import os
import re

def modify_years_in_files(directory):
    # Define the year increment
    year_offset = 2098

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            
            # Read the file content with ANSI encoding
            with open(filepath, 'r', encoding='mbcs') as file:  # 'mbcs' works for ANSI on Windows
                content = file.read()
            
            # Find all occurrences of "is_year = <value>"
            updated_content = re.sub(
                r"(is_year\s*=\s*)(\d+)", 
                lambda match: f"{match.group(1)}{int(match.group(2)) + year_offset}",
                content
            )
            
            # Write the modified content back to the file with ANSI encoding
            with open(filepath, 'w', encoding='mbcs') as file:
                file.write(updated_content)
            
            print(f"Updated years in {filename}")

# Usage
directory_path = r"D:\Program Files\Steam\steamapps\workshop\content\236850\217416366\events"
modify_years_in_files(directory_path)
