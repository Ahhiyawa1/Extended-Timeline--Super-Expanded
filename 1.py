#!/usr/bin/env python
# -*- coding: cp1252 -*-
"""
EU4 Event Optimizer Script (Revised)
-------------------------------------
This script optimizes EU4 1.37X event code by reordering trigger conditions,
adjusting MTTH values, and inserting custom calendar-based is_year fixes.
It preserves localization comments and (as much as possible) the original bracket structure.

For reference:
  https://eu4.paradoxwikis.com/Event_modding
  https://eu4.paradoxwikis.com/Effects
  https://eu4.paradoxwikis.com/Triggers
  https://eu4.paradoxwikis.com/Modifiers
"""

import os
import re

def adjust_year_to_custom_calendar(year):
    offset = 2098
    return year + offset

def reorder_trigger_conditions(inner_content):
    """
    Reorders lines within the trigger block inner content.
    Preserves lines starting with '#' (localisation comments) and reorders others so that
    conditions containing 'has_dlc', 'religion', 'is_year', and 'has_country_flag' come first.
    """
    lines = inner_content.splitlines()
    # Separate comment lines and condition lines, preserving their original indentation.
    comment_lines = [line for line in lines if line.strip().startswith('#')]
    condition_lines = [line for line in lines if not line.strip().startswith('#') and line.strip()]
    
    # Define priority keywords (lowest index = highest priority)
    priority_keys = ['has_dlc', 'religion', 'is_year', 'has_country_flag']
    
    def get_priority(line):
        for idx, key in enumerate(priority_keys):
            if key in line:
                return idx
        return len(priority_keys)
    
    sorted_conditions = sorted(condition_lines, key=get_priority)
    # Combine the original comments (in order) with the sorted conditions.
    return "\n".join(comment_lines + sorted_conditions)

def optimize_mtth_block(inner_content):
    """
    Optimizes the inner content of the mean_time_to_happen block.
    For example, multiply days by 2 and months by 1.5.
    """
    optimized = re.sub(r'(days\s*=\s*)(\d+)', lambda m: m.group(1) + str(int(m.group(2)) * 2), inner_content)
    optimized = re.sub(r'(months\s*=\s*)(\d+)', lambda m: m.group(1) + str(int(float(m.group(2)) * 1.5)), optimized)
    return optimized

def collect_bracket_block(lines, start_index):
    """
    Collects lines from start_index until the block is balanced in terms of braces.
    Returns the block (as a list of lines) and the index of the last line.
    """
    block_lines = []
    open_brackets = 0
    i = start_index
    while i < len(lines):
        line = lines[i]
        # Only count braces if not in a comment.
        if not line.strip().startswith('#'):
            open_brackets += line.count('{')
            open_brackets -= line.count('}')
        block_lines.append(line)
        if open_brackets <= 0:
            break
        i += 1
    # If unbalanced, append missing closing braces.
    if open_brackets > 0:
        block_lines.append("}" * open_brackets + "\n")
    return block_lines, i

def process_event_file(file_path, output_folder):
    """
    Processes a single event file:
      - Optimizes trigger and MTTH blocks by reordering conditions and adjusting time values.
      - Preserves original formatting and bracket structure as much as possible.
    """
    with open(file_path, "r", encoding="cp1252", errors="replace") as f:
        lines = f.readlines()
    
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Check for trigger block
        if re.match(r'^\s*trigger\s*=\s*\{', line):
            block_lines, i = collect_bracket_block(lines, i)
            block_text = "".join(block_lines)
            # Capture the first line (header) and last line (closing brace)
            header = block_lines[0].rstrip("\n")
            closing = block_lines[-1].rstrip("\n")
            # Get inner content (everything except the first and last line)
            if len(block_lines) > 2:
                inner = "".join(block_lines[1:-1])
                optimized_inner = reorder_trigger_conditions(inner)
            else:
                optimized_inner = ""
            new_block = header + "\n" + optimized_inner + "\n" + closing + "\n"
            new_lines.append(new_block)
            i += 1
            continue
        # Check for mean_time_to_happen block
        elif re.match(r'^\s*mean_time_to_happen\s*=\s*\{', line):
            block_lines, i = collect_bracket_block(lines, i)
            block_text = "".join(block_lines)
            header = block_lines[0].rstrip("\n")
            closing = block_lines[-1].rstrip("\n")
            if len(block_lines) > 2:
                inner = "".join(block_lines[1:-1])
                optimized_inner = optimize_mtth_block(inner)
            else:
                optimized_inner = ""
            new_block = header + "\n" + optimized_inner + "\n" + closing + "\n"
            new_lines.append(new_block)
            i += 1
            continue
        else:
            new_lines.append(line)
        i += 1

    output_path = os.path.join(output_folder, os.path.basename(file_path))
    with open(output_path, "w", encoding="cp1252", errors="replace") as f:
        f.writelines(new_lines)
    print(f"Optimized: {os.path.basename(file_path)}")

def main():
    input_folder = "events"  # Change this to your actual input folder path
    output_folder = input_folder + "_optimized"
    os.makedirs(output_folder, exist_ok=True)
    
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".txt"):
            process_event_file(os.path.join(input_folder, file_name), output_folder)
    
    print(f"Optimization complete. Files saved in: {output_folder}")

if __name__ == "__main__":
    main()
