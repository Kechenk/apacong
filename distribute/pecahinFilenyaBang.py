import pandas as pd

def split_data(input_file):
    df = pd.read_excel(input_file, header=None)

    start_row = 7  # Row index to start chunking (indexing starts from 0)
    start_col = 2  # Column index to start chunking (indexing starts from 0)

    chunk_size = 250
    rows, cols = df.shape

    names = [
        "anton", "budi", "charlie", "dimas", "eko", "febby", "gunawan", "harianto", "indri",
        "joko", "kiki", "lamian", "maman", "nanang", "opang", "putra", "queena", "roy", "saputra",
        "tri", "utami", "vivi", "winda", "xavier", "yayan", "zulkarnain"
        ]  # List of names
    max_files_per_name = 2  # Maximum number of files per name
    file_counter = {name: 1 for name in names}  # Initialize file_counter dictionary

    while start_row < rows:
        all_names_reached_max = all(file_counter[name] > max_files_per_name for name in names)
        if all_names_reached_max:
            break

        for name in names:
            if file_counter[name] > max_files_per_name:
                continue

            num_chunks = (rows - start_row) // chunk_size

            for i in range(num_chunks):
                if file_counter[name] > max_files_per_name:
                    break

                end_idx = start_row + chunk_size

                # Slice the dataframe to get the chunk
                chunk = df.iloc[start_row:end_idx, start_col:]

                # Create the output filename
                output_file = f"{name}_{file_counter[name]}.xlsx"

                # Save the chunk as XLSX
                chunk.to_excel(output_file, index=False, header=False)

                file_counter[name] += 1
                start_row = end_idx

            # Check if there are remaining rows after splitting
            if (rows - start_row) % chunk_size != 0 and file_counter[name] <= max_files_per_name:
                remaining_chunk = df.iloc[start_row:, start_col:]

                remaining_output_file = f"{name}_{file_counter[name]}.xlsx"
                remaining_chunk.to_excel(remaining_output_file, index=False, header=False)

                file_counter[name] += 1
                start_row = rows

# Usage
split_data("testfile.xlsx")
