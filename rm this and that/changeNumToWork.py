category_dict = {
    1: "PELAJAR",
    2: "MAHASISWA",
    3: "KARYAWAN SWASTA",
    4: "PNS",
    5: "ASN",
    6: "FREELANCER",
    7: "WIRAUSAHA",
    8: "IBU RUMAH TANGGA",
    9: "LAINNYA",
    10: "GURU",
    11: "Dosen",
    12: "Pelajar SMK",
    13: "Guru SMK",
}

input_file = "./input/kerjo.txt"  # Path to the input text file with numbers
output_file = "./output/kerjoan.txt"  # Path to the output text file to save category labels

with open(input_file, "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]

labels = [category_dict.get(num, "Unknown") for num in numbers]

with open(output_file, "w") as file:
    file.write("\n".join(labels))

print("Category labels saved in", output_file)
