import os
import re

def adjust_year(year):
    """Adds 2098 years to the provided year."""
    try:
        return str(int(year) + 2098)
    except ValueError:
        return year

def process_file(input_file, output_file):
    """Reads a file, adjusts only year parts in dates or is_year = xyz by adding 2098 years, and writes to a new file."""
    with open(input_file, 'r', encoding='ansi') as infile:
        content = infile.read()

    # Pattern to match `is_year = xyz` or dates like `YYYY.MM.DD` where we only want to adjust the year
    pattern = re.compile(r'\bis_year\s*=\s*(\d{1,4})\b|(\d{1,4})\.(\d{1,2})\.(\d{1,2})')

    def adjust_match(match):
        if match.group(1):  # For is_year = xyz
            return f'is_year = {adjust_year(match.group(1))}'
        elif match.group(2):  # For date formatted as YYYY.MM.DD
            adjusted_year = adjust_year(match.group(2))
            return f'{adjusted_year}.{match.group(3)}.{match.group(4)}'
        return match.group(0)  # Just return the original match if no year is found

    # Replace all found patterns
    new_content = re.sub(pattern, adjust_match, content)

    # Write the modified content to the output file
    with open(output_file, 'w', encoding='ansi') as outfile:
        outfile.write(new_content)

def process_directory(input_dir, output_dir):
    """Recursively processes all .txt files in the input directory, adjusts years, and exports to the output directory."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, dirs, files in os.walk(input_dir):
        # Create corresponding output directories
        relative_path = os.path.relpath(root, input_dir)
        output_path = os.path.join(output_dir, relative_path)

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        for file in files:
            if file.endswith(".txt"):
                input_file = os.path.join(root, file)
                output_file = os.path.join(output_path, file)

                # Process each .txt file
                process_file(input_file, output_file)

if __name__ == "__main__":
    input_directory = r"D:\Program Files\Steam\steamapps\common\Europa Universalis IV\history\advisors"  # Change this to your input mod folder
    output_directory = r"D:\Program Files\Steam\steamapps\common\Europa Universalis IV\history\advisors1"  # Change this to your desired output folder

    process_directory(input_directory, output_directory)
