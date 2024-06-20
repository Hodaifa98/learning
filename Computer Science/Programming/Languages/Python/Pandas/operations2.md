# Operations 2
### Truncate
Allows shortening before and/or after specific index values. Useful for selecting a specific range or removing unwanted parts.
```
# Index 2 (exclusive) and after index 5 (inclusive)
truncated_df = df.truncate(before=2, after=5)

# Truncate all rows before the first datetime index
datetime_df = pd.DataFrame({'data': [1, 2, 3]}, index=pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']))

truncated_datetime_df = datetime_df.truncate(before=datetime_df.index[0])
```

### Comparing:
Once combined, DataFrames can be compared using various techniques:

- **Column-wise comparisons:** Use comparison operators (==, !=, <, >, etc.) to compare corresponding columns.

- **Element-wise comparisons:** Use broadcasting with comparison operators for element-wise comparisons between DataFrames with the same shape.

- **Descriptive statistics:** Calculate summary statistics (mean, median, etc.) on each DataFrame and compare the results.

```
ps1 = pd.Series([2.5, 4, 6, 8, 10, 1.75, 40]) 
ps2 = pd.Series([1.5, 3, 5, 7, 10, 1.75, 20]) 

# These compares all elements of the series and display the comparaison for each one.
print(ps1 == ps2)
print(ps1 != ps2)
print(ps1 > ps2)
...

result = ps1.equals(other=ps2) 
print(result)

```
