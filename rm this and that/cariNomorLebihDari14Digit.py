import re

input_file = '50k.txt'
output_file = '50kClean.txt'


with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
    for line_number, line in enumerate(input_file, 1):
        line = line.strip()
        match = re.match(r'^(\d{14})$', line)
        if match:
            number = match.group(1)
            output_file.write(f"{number} (lines: {line_number})\n")
