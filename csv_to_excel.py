import pandas as pd
import os

# loop through all files in current directory
for file in os.listdir():
    if file.endswith(".csv"):
        df = pd.read_csv(file)                      # read CSV
        new_name = file.replace(".csv", ".xlsx")    # new file name
        df.to_excel(new_name, index=False)          # save as XLSX
