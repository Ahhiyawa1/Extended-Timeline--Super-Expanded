import os
import chardet

# Define the target directory
target_directory = r"D:\Users\nomon\Documents\Paradox Interactive\Europa Universalis IV\mod\Extended-Timeline--Super-Expanded\history"

# Recursively walk through the directory
for root, dirs, files in os.walk(target_directory):
    for file in files:
        file_path = os.path.join(root, file)
        
        # Read the file in binary mode for encoding detection
        try:
            with open(file_path, 'rb') as f:
                raw_data = f.read()
                result = chardet.detect(raw_data)
                current_encoding = result['encoding']
        except Exception as e:
            print(f"Failed to read {file_path}: {e}")
            continue

        # Skip files already in Windows-1252
        if current_encoding and current_encoding.lower() in ['windows-1252', 'cp1252']:
            continue

        # Re-encode and overwrite the file with Windows-1252 encoding
        try:
            text = raw_data.decode(current_encoding)
            with open(file_path, 'w', encoding='windows-1252', errors='replace') as f:
                f.write(text)
            print(f"Converted {file_path} from {current_encoding} to Windows-1252")
        except Exception as e:
            print(f"Failed to convert {file_path}: {e}")
