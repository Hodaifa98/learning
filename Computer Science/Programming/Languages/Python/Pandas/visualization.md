
# Visualization

### Using Matplotlib

Matplotlib is a powerful plotting library in Python and can be used directly with pandas DataFrames.

#### Basic Plotting

```python
import matplotlib.pyplot as plt

# Line plot
df.plot(kind='line', x='Date', y='Value')
plt.show()

# Bar plot
df.plot(kind='bar', x='Category', y='Count')
plt.show()
```

#### Customizing Plots

```python
ax = df.plot(kind='line', x='Date', y='Value', title='Line Plot')
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.legend(['Value'])
plt.show()
```

#### Subplots

```python
fig, axes = plt.subplots(nrows=2, ncols=1)

df.plot(kind='line', x='Date', y='Value1', ax=axes[0], title='Value 1')
df.plot(kind='line', x='Date', y='Value2', ax=axes[1], title='Value 2')

plt.tight_layout()
plt.show()
```

### Using Seaborn

Seaborn is another powerful visualization library built on top of matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics.

#### Basic Plotting

```python
import seaborn as sns

# Line plot
sns.lineplot(data=df, x='Date', y='Value')
plt.show()

# Bar plot
sns.barplot(data=df, x='Category', y='Count')
plt.show()
```

#### Customizing Plots

```python
sns.lineplot(data=df, x='Date', y='Value')
plt.title('Line Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
```

#### Multiple Plots

```python
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

sns.lineplot(data=df, x='Date', y='Value1', ax=axes[0])
sns.lineplot(data=df, x='Date', y='Value2', ax=axes[1])

plt.tight_layout()
plt.show()
```

#### Pairplot and Heatmap

```python
# Pairplot
sns.pairplot(df)
plt.show()

# Heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
```

### Choosing the Right Library

- **Matplotlib**: Use for detailed control and customization of plots. Good for creating complex multi-plot figures.
- **Seaborn**: Use for statistical plots and when you need better-looking visualizations with less effort. Excellent for visualizing data distributions and relationships.
