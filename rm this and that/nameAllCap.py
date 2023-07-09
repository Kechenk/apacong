def capitalize_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    modified_content = content.upper()

    with open(file_path, 'w') as file:
        file.write(modified_content)

# Usage
capitalize_words("name.txt")
