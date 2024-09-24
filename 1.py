import os
import re

# Function to convert the date to your custom calendar
def convert_date_to_year(date_str):
    match = re.match(r'(\d{1,4})\.(\d{1,2})\.(\d{1,2})', date_str)
    if match:
        year = int(match.group(1))
        if year >= 1:
            year -= 2098  # Convert AD to custom calendar year
            return f"{year} AD"  # Format for AD
        else:
            year = 2099 - abs(year)  # Handle BC years
            return f"{year} BC"  # Format for BC
    return None

# Function to parse bookmarks and create localization strings
def parse_and_localize_bookmarks(input_dir, output_file):
    localization_entries = []

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.txt'):
                input_file_path = os.path.join(root, file)

                with open(input_file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()

                    # Find bookmark entries
                    bookmark_matches = re.findall(r'bookmark\s*=\s*\{.*?\}', content, re.DOTALL)

                    for bookmark in bookmark_matches:
                        name_match = re.search(r'name\s*=\s*"(.*?)"', bookmark)
                        date_match = re.search(r'date\s*=\s*(\d{1,4}\.\d{1,2}\.\d{1,2})', bookmark)

                        if name_match and date_match:
                            name = name_match.group(1)
                            date_str = date_match.group(1)

                            # Convert date to your custom year system
                            year_formatted = convert_date_to_year(date_str)

                            if year_formatted is not None:
                                # Generate localization string without description
                                localization_entry = f'{name}:0 "{year_formatted}"'
                                localization_entries.append(localization_entry)

    # Write the localization entries to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for entry in localization_entries:
            outfile.write(entry + '\n')

    print(f"Localization entries written to {output_file}")
    
# Set your input directory (common/bookmarks) and output file for localization
input_directory = r'C:\Users\twsb1\Documents\Paradox Interactive\Europa Universalis IV\mod\et_se\common\bookmarks'
output_localization_file = r'C:\Users\twsb1\Documents\Paradox Interactive\Europa Universalis IV\mod\et_se\localisation\bookmarks_l_english.yml'

# Run the function to parse and localize bookmarks
parse_and_localize_bookmarks(input_directory, output_localization_file)

print("Bookmark parsing and localization completed.")
