import os
import re

# Define the path to the country history files folder
COUNTRY_HISTORY_FOLDER = 'C:/Users/twsb1/Documents/Paradox Interactive/Europa Universalis IV/mod/et_se/history/countries'

# Define the government rank to add
GOVERNMENT_RANK = 8

# Regex to match the capital entry
capital_pattern = re.compile(r'(capital\s*=\s*\d+)')

# Regex to match the government_rank entry
government_rank_pattern = re.compile(r'government_rank\s*=\s*\d+')

def add_government_rank(file_path):
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
        # Check if government_rank is already present
        if not government_rank_pattern.search(content):
            # Find the position of the capital entry
            match = capital_pattern.search(content)
            if match:
                insert_position = match.end()
                # Insert government_rank after the capital entry
                updated_content = content[:insert_position] + f'\ngovernment_rank = {GOVERNMENT_RANK}' + content[insert_position:]
                
                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(updated_content)
                print(f"Added government_rank to file: {file_path}")
            else:
                print(f"No capital entry found in file: {file_path}")
        else:
            print(f"government_rank already present in file: {file_path}")

# Process the country files
for country_file in os.listdir(COUNTRY_HISTORY_FOLDER):
    if country_file.endswith('.txt'):
        file_path = os.path.join(COUNTRY_HISTORY_FOLDER, country_file)
        add_government_rank(file_path)

print("Government rank addition complete.")
