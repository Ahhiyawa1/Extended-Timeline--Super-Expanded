import re

def process_gov_data(input_file, output_file):
    def get_value_for_rank(section, rank):
        # Mapping for each section, adjusting value based on rank
        if section == "rank":
            return "COUNTY" if rank <= 7 else "KINGDOM" if rank <= 10 else "DEFAULT"
        elif section in ["ruler_male", "ruler_female"]:
            return "COUNT" if rank <= 7 else "KING" if rank <= 9 else "EMPEROR"
        elif section == "consort_male":
            return "PRINCE_CONSORT"
        elif section == "consort_female":
            return "COUNTESS" if rank <= 7 else "QUEEN" if rank <= 9 else "EMPRESS"
        elif section in ["heir_male", "heir_female"]:
            return "HEIR"
        return "DEFAULT"

    def process_block(block_name, block_lines):
        block_lines = [line.strip() for line in block_lines]
        new_lines = []
        values = [get_value_for_rank(block_name, i) for i in range(1, 11)]

        for i, line in enumerate(block_lines):
            if re.match(r'^\d+ = .+$', line):
                rank_number, _ = line.split('=', 1)
                rank_number = int(rank_number.strip())
                if 1 <= rank_number <= 10:
                    new_lines.append(f"\t\t{rank_number} = {values[rank_number - 1]}\n")
                continue
            new_lines.append(line)
        new_lines.append("}\n")
        return new_lines

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        lines = infile.readlines()
        new_lines = []
        current_block_name = None
        current_block_lines = []

        for line in lines:
            stripped_line = line.strip()
            if stripped_line.endswith('= {'):
                if current_block_name:
                    new_lines.extend(process_block(current_block_name, current_block_lines))
                current_block_name = stripped_line.split(' =')[0].strip()
                current_block_lines = [line]
            elif stripped_line == '}':
                current_block_lines.append(line)
                if current_block_name:
                    new_lines.extend(process_block(current_block_name, current_block_lines))
                current_block_name = None
                current_block_lines = []
            else:
                if current_block_name:
                    current_block_lines.append(line)
                else:
                    new_lines.append(line)

        if current_block_name:
            new_lines.extend(process_block(current_block_name, current_block_lines))

        outfile.writelines(new_lines)

# Example usage
input_txt = 'input.txt'  # Your input file with government definitions
output_txt = 'output.txt'  # Output file with the updated data
process_gov_data(input_txt, output_txt)
