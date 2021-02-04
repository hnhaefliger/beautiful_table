# beautiful_table
Print table-like data one row at a time in python without the formatting and alignment annoyances

```python3
import beautiful_table

table = beautiful_table.BeautifulTable(['col1', 'col2', 'col3']) # most basic table

for i in range(10):
    table.printrow([i for j in range(3)])
```

```python3
import beautiful_table

table = beautiful_table.BeautifulTable(['row name', 'col1', 'col2', 'col3'], padding=2, maxes=10)

for i in range(10):
    table.printrow([i for j in range(3)])
```

```python3
import beautiful_table

table = beautiful_table.BeautifulTable(['row name', 'col1', 'col2', 'col3'], padding=2, maxes=[20, 10, 10, 10])

for i in range(10):
    table.printrow([i for j in range(3)])
```
