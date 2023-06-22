import pandas as pd
from openpyxl import load_workbook

def merge_data(input_files, output_file, template_file):
    # Load the template file
    template = load_workbook(template_file)

    for input_file in input_files:
        # Extract the name from the input file name
        name = input_file.split("_")[0]

        # Get the corresponding sheet in the template file
        sheet = template[name]

        # Load the input file data
        df = pd.read_excel(input_file, header=None)

        # Get the data range in the input file
        data_range = df.loc[:249, :7].values.tolist()

        # Get the starting cell in the template sheet based on the sheet name
        start_cell = template[name]['C10']

        # Copy the data to the template sheet
        for r, row in enumerate(data_range):
            for c, value in enumerate(row):
                sheet.cell(row=start_cell.row + r, column=start_cell.column + c).value = value

    # Save the modified template file
    template.save(output_file)
    print(f"Merged data saved to: {output_file}")

# Usage
input_files = ["anton_1.xlsx", "anton_2.xlsx", "budi_1.xlsx", "budi_2.xlsx"]
output_file = "merged_data.xlsx"
template_file = "templateabsen.xlsx"

merge_data(input_files, output_file, template_file)
