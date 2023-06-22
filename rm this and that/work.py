import random

loop = 1000
krywn_count = int(loop * 0.30)
freelance_count = int(loop * 0.20)
mak_count = int(loop* 0.15)
lain_count = int(loop * 0.20)
wirausaha_count = loop - krywn_count - freelance_count - mak_count - lain_count

string = ["KARYAWAN SWASTA"] * krywn_count + ["FREELANCE"] * freelance_count + ["IBU RUMAH TANGGA"] * mak_count +["LAINNYA"] * lain_count + ["WIRAUSAHA"] * wirausaha_count
random.shuffle(string)

file_name = "kerjoan.txt"
with open(file_name, 'w')as file:
    for string in string:
        file.write(string + "\n")

print("kesimpen nak", file_name) 

    