import os
import re

# Define the path to the mod folder
MOD_FOLDER_PATH = 'C:/Users/twsb1/Documents/Paradox Interactive/Europa Universalis IV/mod/et_se'

# Folders to exclude from processing
EXCLUDE_FOLDERS = ['events', 'decisions', 'history']

# Define the conversion function
def convert_to_custom_calendar(year):
    if year < 1:
        return f"{2100 + year - 1}"
    else:
        return f"{year + 2098}"

# Regex to match and capture dates in the format 'yyyy.mm.dd'
date_pattern = re.compile(r'date\s*=\s*(\d{1,4})\.(\d{1,2})\.(\d{1,2})')

def convert_file_dates(file_path):
    content = None
    # Attempt to read the file with UTF-8 encoding first
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        # If UTF-8 fails, try ISO-8859-1 encoding
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            content = file.read()

    if content is not None:
        def replace_date(match):
            year = int(match.group(1))
            month = match.group(2)
            day = match.group(3)
            custom_year = convert_to_custom_calendar(year)
            return f"date = {custom_year}.{month}.{day}"

        updated_content = date_pattern.sub(replace_date, content)

        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            print(f"Updated dates in file: {file_path}")
        else:
            print(f"No date changes needed in file: {file_path}")

# Function to traverse directories and process files
def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print(f"Processing file: {file_path}")
            convert_file_dates(file_path)

# Process all directories except those in EXCLUDE_FOLDERS
for folder_name in os.listdir(MOD_FOLDER_PATH):
    if folder_name not in EXCLUDE_FOLDERS:
        folder_path = os.path.join(MOD_FOLDER_PATH, folder_name)
        if os.path.isdir(folder_path):
            process_directory(folder_path)

print("Date conversion complete.")
