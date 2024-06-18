import os
import re

# Define the path to the bookmarks wip folder
BOOKMARKS_WIP_FOLDER = 'C:/Users/twsb1/Documents/Paradox Interactive/Europa Universalis IV/mod/et_se/common/bookmarks/wip'

# Define the conversion function
def convert_to_custom_calendar(year):
    if year < 1:
        return f"{2100 + year - 1}"
    else:
        return f"{year + 2098}"

# Regex to match and capture 'date = yyyy.mm.dd'
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

# Function to traverse directory and process files
def process_directory(directory_path):
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            print(f"Processing file: {file_path}")
            convert_file_dates(file_path)

# Process the bookmarks wip folder
process_directory(BOOKMARKS_WIP_FOLDER)

print("Date conversion complete.")
