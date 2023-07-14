file_path = "mail.txt"
output_file_path = "modified_mail.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

modified_lines = [line.strip() + "@anu.com" for line in lines]

with open(output_file_path, "w") as output_file:
    output_file.write("\n".join(modified_lines))

print("Emails modified and saved to 'modified_mail.txt'")
