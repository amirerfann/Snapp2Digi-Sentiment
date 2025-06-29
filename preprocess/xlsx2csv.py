import pandas as pd

# Read the Excel file into a DataFrame
excel_file = 'data/comment.xlsx'
df = pd.read_excel(excel_file)

# Write the DataFrame to a CSV file
csv_file = 'digikala.csv'
df.to_csv(f"data/{csv_file}", index=False)