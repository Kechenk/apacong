input_filename = 'num.txt'
output_filename = 'rmNum.txt'
duplicates = {}
lines = []

# Read input file and process lines
with open(input_filename, 'r') as input_file:
    for line_num, line in enumerate(input_file, start=1):
        line = line.strip()
        lines.append(line)
        if line in duplicates:
            duplicates[line].append(line_num)
        else:
            duplicates[line] = [line_num]

# Modify lines to replace subsequent duplicate occurrences with "rm"
for i in range(len(lines)):
    line = lines[i]
    if len(duplicates[line]) > 1 and i != duplicates[line][0] - 1:
        lines[i] = 'rm'

# Write output file
with open(output_filename, 'w') as output_file:
    for line in lines:
        output_file.write(line + '\n')

print("Duplicate occurrences replaced with 'rm' in", output_filename)

# Write duplicate occurrences to separate output file
duplicates_output_filename = 'numduplicates.txt'
with open(duplicates_output_filename, 'w') as duplicates_output_file:
    for line, line_nums in duplicates.items():
        if len(line_nums) > 1:
            duplicates_output_file.write(f"{line} (line {', '.join(map(str, line_nums))})\n")

print("Duplicate occurrences saved to", duplicates_output_filename)
