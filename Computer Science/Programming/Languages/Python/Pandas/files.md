# Working with files

### csv:
```
import pandas as pd

df = pd.read_csv("data.csv")
```

Many parameters can be passed, such as:
- **sep**: Character for delimter.
- **usecols**: Define subset of columns to select
- **nrows**: Number of rows to read.
- ...

**Exporting a dataframe as a csv:**

```df.to_csv('file1.csv')```

### Excel:
```
excel_file = pd.ExcelFile('data.xlsx')

# Sheet names
print(excel_file.sheet_names) 

# Load a sheet as a dataframe
df = excel_file.parse('Sheet1') 

# Read specific columns from  
df = pd.read_excel('data.xlsx', usecols = [0, 3])

# Read all sheets
all = pd.read_excel('data.xlsx', na_values = "Missing", sheet_name = None)
```
