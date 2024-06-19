# Pandas Series
Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.).

The axis labels are called index.
Labels don't need to be unique but must be a hashable type. The object supports both integer and label-based indexing.

### Creating a series:

```
import pandas as pd

# From list.
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ser = pd.Series(data)
```

### Access an element:
Position access:
```
first_element = ser[0]
first_5_elements = ser[:5]
```

Label (index) access:
```
data = ['a', 'b']
# Indexes could be an integer too.
ser = pd.Series(data,index=['e1', 'e2'])
e1 = ser['e1']
```

Using **.loc** and **.iloc**: 

.loc is a function that selects data by index. It can select subsets of data.

``` ser.loc[3:6]```

.iloc is similar to .loc but only uses integer locations.

``` ser.iloc[3:6]```

### Operations on series:
There are many binary operations (add, sub, mul, div, sum, abs...).

```
ser1 = pd.Series([5, 2], index=['a', 'b'])
ser2 = pd.Series([1, 6], index=['a', 'b'])

# Add
ser1.add(ser2, fill_value=0)

# Substract
ser1.sub(ser2, fill_value=0)
```

### Conversion operations:
We can convert the datatype of a series (int, string, list...).

```
data = pd.read_csv("data.csv") 
    
# Dropping null value columns to avoid errors
data.dropna(inplace = True) 
   
# Storing dtype before converting
before = data.dtypes 
   
# Converting dtypes using astype 
data["Name"]= data["Name"].astype(str) 
data["Age"]= data["Age"].astype(int) 
```

### Series methods:
**Series()**     => Create a series.

**size()**       => Number of elements in data.

**head()**       => Return specific number of rows from beginning.

**eq()**         => Compare equality.
....