from collections import defaultdict

input_filename = 'num.txt'
output_filename = 'output.txt'
duplicates = defaultdict(list)

with open(input_filename, 'r') as input_file:
    for line_number, line in enumerate(input_file, 1):
        data = line.strip()
        duplicates[data].append(line_number)

# Extract duplicate entries along with line numbers
duplicate_entries = [(entry, line_numbers) for entry, line_numbers in duplicates.items() if len(line_numbers) > 1]
total_duplicates = sum(len(line_numbers) for _, line_numbers in duplicate_entries)

# Write duplicate entries to output file
with open(output_filename, 'w') as output_file:
    for entry, line_numbers in duplicate_entries:
        line_numbers_str = ', '.join(str(line_number) for line_number in line_numbers)
        output_file.write(f"{entry} (lines: {line_numbers_str})\n")

print("Duplicate entries saved to", output_filename)
print("Total duplicate entries:", total_duplicates)
