import pandas as pd
from openpyxl import load_workbook

def merge_data(input_files, output_file, template_file):
    template = load_workbook(template_file)

    for input_file in input_files:
        name = input_file.split("_")[0]

        # Mengubah nama sheet menjadi lowercase
        sheet_name = name.lower()

        # Mengecek jika nama sheet sudah ada, jika tidak ada, tambahkan sheet baru
        if sheet_name not in template.sheetnames:
            template.create_sheet(sheet_name)

        sheet = template[sheet_name]

        df = pd.read_excel(input_file, header=None)

        data_range = df.loc[:249, :9].values.tolist()

        start_cell = sheet['B10']

        for r, row in enumerate(data_range):
            for c, value in enumerate(row):
                sheet.cell(row=start_cell.row + r, column=start_cell.column + c).value = value

    template.save(output_file)
    print(f"Merged data saved to: {output_file}")

# Penggunaan
input_files = [
    "1_1.xlsx", "2_1.xlsx", "3_1.xlsx", "4_1.xlsx", "5_1.xlsx", "6_1.xlsx",
    "7_1.xlsx", "8_1.xlsx", "9_1.xlsx", "10_1.xlsx", "11_1.xlsx", "12_1.xlsx",
    "13_1.xlsx", "14_1.xlsx", "15_1.xlsx", "16_1.xlsx", "17_1.xlsx", "18_1.xlsx",
    "19_1.xlsx", "20_1.xlsx", "21_1.xlsx", "22_1.xlsx", "23_1.xlsx", "24_1.xlsx",
    "25_1.xlsx", "26_1.xlsx", "27_1.xlsx", "28_1.xlsx", "29_1.xlsx", "30_1.xlsx",
    "31_1.xlsx", "32_1.xlsx", "33_1.xlsx", "34_1.xlsx", "35_1.xlsx", "36_1.xlsx"
]

output_file = "Absensi Komunitas 07-08.xlsx"
template_file = "templateabsen.xlsx"

merge_data(input_files, output_file, template_file)
