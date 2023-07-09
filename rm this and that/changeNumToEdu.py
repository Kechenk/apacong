category_dict = {
    4:  "SD",
    5:  "SMP",
    6:  "SMA",
    7:  "D1",
    8:  "D2",
    9:  "D3",
    10: "S1",
    11: "S2",
    12: "S3"
}

input_file = "./input/cekulah.txt"  # Path to the input text file with numbers
output_file = "./output/sekolah.txt"  # Path to the output text file to save category labels

with open(input_file, "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]

labels = [category_dict.get(num, "Unknown") for num in numbers]

with open(output_file, "w") as file:
    file.write("\n".join(labels))

print("Category labels saved in", output_file)