import re

def convert_color(match):
    # Extract the floating-point RGB values
    r, g, b = map(float, match.group(1).split())
    
    # Convert to 0-255 range and round
    r, g, b = round(r * 255), round(g * 255), round(b * 255)
    
    # Return the new format, ensuring proper scaling
    return f'color = {{ {r} {g} {b} }}'

def process_religion_file(input_file, output_file):
    with open(input_file, 'r', encoding='ANSI') as f:
        content = f.read()
    
    # Regex to find color definitions only in normalized format
    pattern = re.compile(r'color\s*=\s*\{\s*([0-1]?[0-9]?\.?[0-9]*\s+[0-1]?[0-9]?\.?[0-9]*\s+[0-1]?[0-9]?\.?[0-9]*)\s*\}')
    
    # Replace normalized RGB values with standard RGB (0-255) without affecting already converted values
    updated_content = pattern.sub(lambda m: convert_color(m) if any('.' in num for num in m.group(1).split()) else m.group(0), content)
    
    with open(output_file, 'w', encoding='ANSI') as f:
        f.write(updated_content)

# Example usage
input_file = '00_religion.txt'  # Change this to your actual file
output_file = '00_religion.txt'
process_religion_file(input_file, output_file)
print("Conversion complete! Output saved to:", output_file)
