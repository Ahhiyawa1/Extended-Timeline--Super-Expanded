import os
import re

def fix_dates_in_file(file_path, year_adjustment):
    # Read the file with the correct encoding and handle errors
    with open(file_path, 'r', encoding='cp1252', errors='replace') as file:
        content = file.read()
    
    # Regular expression to find date patterns in the format YYYY.M.D, YY.M.D, or even Y.M.D
    date_pattern = re.compile(r'\b(\d{1,4})\.(\d{1,2})\.(\d{1,2})\b')
    
    def adjust_date(match):
        year, month, day = map(int, match.groups())
        
        # Adjust only if the year is below 2099
        if year < 2099:
            new_year = year + year_adjustment
        else:
            new_year = year
        
        return f'{new_year}.{month}.{day}'

    # Replace all dates using the regex
    new_content = date_pattern.sub(adjust_date, content)
    
    # Write the file with the correct encoding and handle errors
    with open(file_path, 'w', encoding='cp1252', errors='replace') as file:
        file.write(new_content)

def process_directory(input_directory, year_adjustment):
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                fix_dates_in_file(file_path, year_adjustment)

if __name__ == "__main__":
    # Updated input directory as per your request
    input_directory = "C:/Users/twsb1/Documents/Paradox Interactive/Europa Universalis IV/mod/et_se/history/countries"
    year_adjustment = 2098
    process_directory(input_directory, year_adjustment)
    print("Date adjustment complete.")
