import pandas as pd
import glob

filepaths = glob.glob("Invoices\*.xlsx")
print(filepaths)

for file in filepaths:
    print(file)
    df = pd.read_excel(file, sheet_name='Sheet 1')
    print(df)