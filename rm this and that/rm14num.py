import re

def remove_last_string_if_number_14_digits(number):
    return str(number)[:-1] if len(str(number)) == 14 else str(number)

with open('num.txt', 'r') as file:
    lines = file.readlines()

processed_lines = []
for line in lines:
    number = line.strip()
    processed_number = remove_last_string_if_number_14_digits(number)
    processed_lines.append(f"{processed_number}\n")

with open('output.txt', 'w') as file:
    file.writelines(processed_lines)

print("Output file generated: output.txt")
