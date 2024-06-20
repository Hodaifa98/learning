# Rows and columns in Dataframes
A dataframe is a two dimensional data structure (rows and columns). Basic operations can be performed.

```
import pandas as pd

data = {
        'Name': ['A', 'B'],
        'Age': [25, 30],
        'Address': ['Ct1', 'Ct2']}
df = pd.DataFrame(data)
```

### Columns:
#### Select two columns:
```df[['Name', 'Address']]```

#### Replace a column:
```
new_address = ['Ct3', 'Ct4']
df['Address'] = new_address
```

#### Drop a column:
```
# inplace=True | Original dataframe will be modified
df.drop(["Age", "Address"], axis=1, inplace=True)
```

#### Slicing columns:
```
# By name
selected = df[['Name', 'Address']]

# Range (from 1 (inclusive) to 2 (exclusive))
selected = df.iloc[:, 1:3]

# From starting point (from 1 inclusive)
selected = df.iloc[:, 1:]

# Until end point (Up to index 3 inclusive)
selected = df.iloc[:, :4]
```

### Rows:
#### Select rows:
```
# With index
df.loc[0]

# With condition
df.loc[df["Age"] == 25]
```

#### Add a row:
```
new_row = {'Name': 'C', 'Age': 35}
df = df.append(new_row, ignore_index=True)
```

#### Drop a row:
```
index_to_drop = 1
df = df.drop(index_to_drop, axis=0)
```

#### Modify a row:
```
index_to_modify = 0
df.loc[index_to_modify, 'Name'] = 'D'

# Update all columns
df['Age'] = df['Age'] + 1
```

#### Sort:
```df_sorted = df.sort_values(by='Age', ascending=False)```

#### Group & aggregate:
```name_wise_average_age = df.groupby('Name')['Age'].mean()```
