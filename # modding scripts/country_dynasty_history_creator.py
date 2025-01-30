import requests
from bs4 import BeautifulSoup
import random
import re

# === Custom Calendar Conversion ===
def convert_to_custom_year(year):
    """Convert historical BC/AD year to custom year with Year 0"""
    if year < 0:  # BC Years
        return 2098 - abs(year)  # Year 0 included
    return 2098 + year  # AD Years

# === EU4 History Entry Generator ===
def generate_history_entry(date, ruler_type, name, dynasty, adm, dip, mil, birth_date=None, death_date=None, claim=None, female=False):
    """Generate EU4 formatted history entry with female monarch logic"""
    # Default dates if no day/month is specified
    if birth_date is None:
        birth_date = f"{date.split('.')[0]}.1.1"  # Default to 1st of January
    if death_date is None:
        death_date = f"{date.split('.')[0]}.1.1"  # Default to 1st of January

    entry = f"{date} = {{\n\t{ruler_type} = {{\n\t\tname = \"{name}\""
    if ruler_type == "heir":
        entry += f"\n\t\tmonarch_name = \"{name}\""
    entry += f"\n\t\tdynasty = \"{dynasty}\""
    entry += f"\n\t\tadm = {adm}\n\t\tdip = {dip}\n\t\tmil = {mil}"
    if female:
        entry += "\n\t\tfemale = yes"
    entry += f"\n\t\tbirth_date = {birth_date}\n\t\tdeath_date = {death_date}"

    if claim:
        entry += f"\n\t\tclaim = {claim}"
    entry += "\n\t}\n}\n"
    return entry

# === Wikipedia Scraping Function ===
def scrape_wikipedia_monarch_data(url):
    """Scrape monarch list and data from Wikipedia"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    monarchs = []
    # Parse Wikipedia table
    for row in soup.find_all('table', class_='wikitable')[0].find_all('tr')[1:]:  # Find the monarch table
        cols = row.find_all('td')
        
        # Ensure that the row contains at least 4 columns (name, dynasty, reign start, and reign end)
        if len(cols) >= 4:
            name = cols[0].get_text(strip=True)
            dynasty = cols[1].get_text(strip=True)
            reign_start = cols[2].get_text(strip=True)
            reign_end = cols[3].get_text(strip=True)
            gender = 'female' if 'Queen' in name or 'Empress' in name else 'male'  # Logic for female monarchs

            # Convert reign_start to valid year
            start_year = None
            if 'BC' in reign_start:
                try:
                    start_year = convert_to_custom_year(int(reign_start.split(' ')[0]) * -1)  # Handle BC
                except ValueError:
                    print(f"Skipping invalid reign start year: {reign_start}")
            else:
                try:
                    start_year = convert_to_custom_year(int(reign_start.split(' ')[0]))  # AD
                except ValueError:
                    print(f"Skipping invalid reign start year: {reign_start}")

            if start_year is None:
                continue  # Skip this entry if the year couldn't be parsed

            # Convert reign_end to valid year
            end_year = None
            if 'BC' in reign_end:
                try:
                    end_year = convert_to_custom_year(int(reign_end.split(' ')[0]) * -1)  # Handle BC
                except ValueError:
                    print(f"Skipping invalid reign end year: {reign_end}")
            else:
                try:
                    end_year = convert_to_custom_year(int(reign_end.split(' ')[0]))  # AD
                except ValueError:
                    print(f"Skipping invalid reign end year: {reign_end}")

            if end_year is None:
                end_year = start_year  # Default to start year if end year isn't valid

            # Adjust for missing values or assign random values
            adm, dip, mil = random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)
            monarchs.append({
                "name": name,
                "dynasty": dynasty,
                "start_year": start_year,
                "end_year": end_year,
                "adm": adm,
                "dip": dip,
                "mil": mil,
                "gender": gender
            })
        else:
            print(f"Skipping row with insufficient columns: {row}")
    return monarchs



# === Main Function ===
def generate_dynasty_history():
    # Get the URL for the monarch data from Wikipedia or similar source
    country_tag = input("Enter the country tag (e.g., PT0 for Ptolemaic Egypt): ").strip().upper()
    url = input("Enter the Wikipedia URL of the monarch list (e.g., https://en.wikipedia.org/wiki/Ptolemaic_dynasty): ").strip()

    # Scrape the monarch data from the provided URL
    monarchs = scrape_wikipedia_monarch_data(url)

    history_entries = []
    for monarch in monarchs:
        # Insert gender-based logic for female monarch
        female = monarch['gender'] == 'female'
        monarch_entry = generate_history_entry(f"{monarch['start_year']}.1.1", "monarch", monarch['name'], monarch['dynasty'], monarch['adm'], monarch['dip'], monarch['mil'], female=female)
        history_entries.append(monarch_entry)

        # Optionally generate heirs if applicable (random)
        if random.choice([True, False]):
            heir_name = f"{monarch['name']} Jr."
            heir_entry = generate_history_entry(f"{monarch['start_year'] + random.randint(10, 30)}.1.1", "heir", heir_name, monarch['dynasty'], random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), claim=random.randint(50, 100))
            history_entries.append(heir_entry)

    # Save the output to a file in Western 1252 encoding (ANSI)
    filename = f"{country_tag}_dynasty_history.txt"
    with open(filename, "w", encoding="1252") as file:
        file.writelines(history_entries)

    print(f"? Dynasty history saved to **{filename}**")

# === Running the Script ===
if __name__ == "__main__":
    generate_dynasty_history()
