import os
import re

# Define the path to the mod folder
MOD_FOLDER_PATH = 'C:/Users/twsb1/Documents/Paradox Interactive/Europa Universalis IV/mod/et_se'

# Folder to process
FOLDER_TO_PROCESS = 'common/religions'

# Define the conversion function
def convert_to_custom_calendar(year):
    if year < 1:
        return f"{2100 + year - 1}"
    else:
        return f"{year + 2098}"

# Regex to match and capture 'is_year = XYZ'
is_year_pattern = re.compile(r'(\bis_year\s*=\s*)(\d{1,4})')

def convert_file_years(file_path):
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
        def replace_year(match):
            prefix = match.group(1)
            old_year = int(match.group(2))
            custom_year = convert_to_custom_calendar(old_year)
            return f"{prefix}{custom_year}"

        updated_content = is_year_pattern.sub(replace_year, content)

        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            print(f"Updated years in file: {file_path}")
        else:
            print(f"No year changes needed in file: {file_path}")

# Function to process files in the specified folder
def process_folder(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            print(f"Processing file: {file_path}")
            convert_file_years(file_path)

# Construct full path to the folder to process
folder_to_process_path = os.path.join(MOD_FOLDER_PATH, FOLDER_TO_PROCESS)

# Process the specified folder
process_folder(folder_to_process_path)

print("Year conversion complete.")
