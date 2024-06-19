# Pandas

Open-source library package built on top of NumPy.

Offers various data structures and operations for numerical data manipulation.

### Data frames
A DataFrame is created by loading datasets from: SQL, CSV, Excel, Lists, Dictionaries...
Resemble spreadsheets with rows and columns for organizing data.
DataFrames can store different data types like text, numbers, and dates.
You can perform calculations, select specific data subsets, and add/remove rows and columns to manipulate data efficiently.

##### Creating a dataframe:
```
imports pandas as pd

# Empty.
df1 = pd.DataFrame()

# One dimension list.
lst = ["A", "B", "C]
df2 = pd.DataFrame(lst)

# Array.
dt = {'Name':['A', 'B'], 'Age':[20, 21]}
df3 = pd.DataFrame(dt)
```

##### Describe a dataframe:
It displays several statistical measures, including mean, median, standard deviation...
```
import pandas as pd
data = pd.read_csv('data.csv')

print(data.descibe())
```