import pandas as pd

def change_prefix_to_zero(number):
    return f"=CONCATENATE('0', {number})"

with open('test.txt', 'r') as file:
    lines = file.readlines()

processed_lines = []
for line in lines:
    number = line.strip()
    processed_number = change_prefix_to_zero(number)
    processed_lines.append(processed_number)

df = pd.DataFrame(processed_lines, columns=['Formula'])
output_file = 'output.xlsx'
df.to_excel(output_file, index=False)

print(f"Output file generated: {output_file}")
