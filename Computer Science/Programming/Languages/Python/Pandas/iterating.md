# Iterating Through DataFrames

### Using iterrows():
This method iterates over each row as a pandas Series with its index as the key.

```
for index, row in df.iterrows():
  # Access row elements using index/column names
  print(f"Index: {index}, Name: {row['Name']}, Age: {row['Age']}")
```

### Looping through Columns:
```
for col in df.columns:
  # Process each column's data
  print(f"Column: {col}, Values: {df[col].tolist()}")
```

### Using apply() (Row-wise):

Apply a function to each row (similar to iterrows but with more control):

```
def process_row(row):
  # Perform operations on the row
  return row * 2  # Example: Double each value

df_processed = df.apply(process_row, axis=1)  # axis=1 for rows
```

#### Choosing the Right Method:

- Use iterrows() for row-by-row processing and accessing row data.
- Use column looping for simpler column-wise operations.
- Use apply (with axis=1) for row-wise transformations with custom functions.