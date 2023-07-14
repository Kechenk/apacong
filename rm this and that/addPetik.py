import re

def input(num):
	return str(num)[:+1] if len(str(num)) == 14 else str(num)

	with open('num.txt', 'r') as file:
		lines = file.readlines()

processed_lines = []
for line in lines:
	num = line.strip()
	processed_number = input(num)
	processed_lines.append(f"'{processed_number}\n")

	with open('output.txt', 'w') as file:
		file.writelines(processed_lines)

print("wes")