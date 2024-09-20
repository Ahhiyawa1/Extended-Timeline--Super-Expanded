import os
import re

def add_government_rank(file_path):
    # Read the file with the correct encoding and handle errors
    with open(file_path, 'r', encoding='cp1252', errors='replace') as file:
        content = file.read()

    # Skip if file is empty or already contains 'government_rank'
    if not content.strip() or 'government_rank' in content:
        return
    
    # Insert 'government_rank = 8' before the 'history' section
    new_content = re.sub(r'(government = .*?)\n(?=\w+)', r'\1\ngovernment_rank = 8\n', content, count=1)
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='cp1252', errors='replace') as file:
        file.write(new_content)

def process_directory(input_directory):
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                add_government_rank(file_path)

if __name__ == "__main__":
    input_directory = "C:/Users/twsb1/Documents/Paradox Interactive/Europa Universalis IV/mod/et_se/history/countries"
    process_directory(input_directory)
    print("Government rank addition complete.")
