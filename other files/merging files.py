import pandas as pd

# Load CSV files with correct encoding and skip metadata rows
df_eng = pd.read_csv(
    'eng.csv', 
    encoding='latin1',  # Handle special characters like ©
    skiprows=0,         # Skip metadata rows at the top
    thousands=',',      # Handle commas in numbers if needed
    na_values=['-', ''] # Treat hyphens/blanks as NaN
)


df_pak = pd.read_csv( 
    'pak.csv', 
    encoding='latin1', 
    skiprows=0,         
    thousands=',',      
    na_values=['-', ''] 
)

# Create Excel file with both sheets
with pd.ExcelWriter('combined_data.xlsx', engine='openpyxl') as writer:
    df_pak.to_excel(writer, sheet_name='Pakistan_Weather', index=False)
    df_eng.to_excel(writer, sheet_name='UK_Breastfeeding', index=False)