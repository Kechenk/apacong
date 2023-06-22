import pandas as pd
from datetime import datetime

file_path = "500k2.csv"

# Read Data
parsed_data = []
skipped_lines = []
with open(file_path, "r") as file:
    for line in file:
        try:
            line_data = line.strip().split(",")
            if len(line_data) >= 5:
                dob = line_data[2].strip() if len(line_data) > 2 else ""
                age = ""  # Initialize age as empty string
                if dob:
                    # Calculate age based on date of birth
                    dob_date = datetime.strptime(dob, "%Y-%m-%d")  # Assuming the date format is YYYY-MM-DD
                    today = datetime.today()
                    age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))

                entry = {
                    "EMAIL": line_data[0].strip(),
                    "NAME": line_data[1].strip(),
                    "AGE": age,
                    "PHONE": line_data[3].strip() if len(line_data) > 3 else "",
                    "SHA384": line_data[4].strip() if len(line_data) > 4 else "",
                }
                parsed_data.append(entry)
            else:
                skipped_lines.append(line.strip())
        except Exception:
            skipped_lines.append(line.strip())

# Create a DataFrame from the parsed data
df = pd.DataFrame(parsed_data)

# Sort the DataFrame based on the presence of the email field
df_sorted = df[df["EMAIL"].str.contains("@")]

# Export the DataFrame to an Excel file
df_sorted.to_excel("500k2.xlsx", index=False)

# Export the skipped lines to a separate Excel file
df_skipped = pd.DataFrame({"Skipped Lines": skipped_lines})
df_skipped.to_excel("purged500k2.xlsx", index=False)
