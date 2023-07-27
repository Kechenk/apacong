def remove_sobatlama(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    processed_lines = [line.replace('@heysobat.com', '') for line in lines]

    with open(output_file, 'w') as file:
        file.writelines(processed_lines)

    print(f"Processed file saved to: {output_file}")

# Usage
input_file = 'mail.txt'
output_file = 'mail_clean.txt'
remove_sobatlama(input_file, output_file)