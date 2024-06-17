import os

# Define the replacements as a dictionary
replacements = {
    'government_rank = 3': 'government_rank = 10',
    'government_rank = 2': 'government_rank = 8',
    'government_rank = 1': 'government_rank = 4'
}

def replace_or_add_government_rank(file_path):
    """Reads a file, replaces government_rank values, adds government_rank if missing, and writes back the changes."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if any government_rank is present
    if 'government_rank = ' not in content:
        # If not, add government_rank = 8 at the end of the file
        content += '\ngovernment_rank = 8\n'
    
    for old, new in replacements.items():
        content = content.replace(old, new)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_directory(directory):
    """Recursively processes all files in the given directory and its subdirectories."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):  # Process only .txt files
                file_path = os.path.join(root, file)
                replace_or_add_government_rank(file_path)

# Define the path to your mod's history folder
mod_history_folder = 'C:/Users/twsb1/Documents/Paradox Interactive/Europa Universalis IV/mod/et_se/history'

# Process the directory
process_directory(mod_history_folder)

print("Replacement complete.")
