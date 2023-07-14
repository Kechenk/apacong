def change_prefix_to_zero(number):
    return number.replace('62', '0', 1)

with open('test.txt', 'r') as file:
    lines = file.readlines()

processed_lines = []
for line in lines:
    number = line.strip()
    processed_number = change_prefix_to_zero(number)
    processed_lines.append(f"'{processed_number}\n")

with open('output.txt', 'w') as file:
    file.writelines(processed_lines)

print("Output file generated: output.txt")
