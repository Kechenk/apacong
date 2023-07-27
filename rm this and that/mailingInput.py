def input(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    processed_lines = []

    for line in lines:
        # Replace "testing1" with the content from the txt file
        email = line.strip()  # Assuming the content of txt filmaile contains only the email
        processed_line = f'createDelayedEmail("{email}", "sUR4B4Y4123!@#", "2", "heysobat.com");\n'
        processed_lines.append(processed_line)

    with open(output_file, 'w') as file:
        file.writelines(processed_lines)

    print(f"Processed file saved to: {output_file}")

# Usage
input_file = 'mail.txt'
output_file = 'mail_out.txt'
input(input_file, output_file)
