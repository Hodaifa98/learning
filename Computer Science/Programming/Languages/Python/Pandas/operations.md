# Operations
apply() is more general, allowing any custom function.

aggregate() focuses on summary statistics by group.

mean() is a specific function for calculating the average.


### apply
Applies a function element-wise to each column or row in a DataFrame.
Useful for custom transformations or cleaning data.
```
def standardize_name(name):
  return name.lower().strip()

df['Clean_Name'] = df['Name'].apply(standardize_name)
```

```
# Inline function to add a grade based on score
df['Grade'] = df['Score'].apply(lambda score: 'A' if score >= 90 else ('B' if score >= 80 else 'C'))
```

### aggregate
Computes summary statistics for each group (similar to .groupby).
Can accept different functions for different columns.
```
stats = df.groupby('Age').aggregate({'Name': 'count', 'Age': 'mean'})
```

### mean
Calculates the mean (average) of a Series or column.

```average_age = df['Age'].mean()```

### isin
Checks for membership in a specific set of values within a DataFrame column.
```
selected_names = df[df['Name'].isin(['A', 'B'])]
```

### fillna
Replaces missing values (NaN) in a DataFrame with a specified value.
```df['Age'].fillna(0, inplace=True)```

### pivot_table
Creates a concise summary table with aggregation functions applied to groups defined by columns.

```
# Group by 'Name' and calculate average 'Age' and sum of 'Score'
summary = df.pivot_table(index='Name', values=['Age', 'Score'], aggfunc={'Age': 'mean', 'Score': 'sum'})
```
