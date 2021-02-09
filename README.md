# beautiful_table

Print table-like data one row at a time in python without the formatting and alignment annoyances

## Table formatting

Basic Table

```python3
import beautiful_table

table = beautiful_table.BeautifulTable(['col1', 'col2', 'col3'])

for i in range(5):
    table.printrow([i for j in range(3)])
```
```
col1  col2  col3
0     0     0   
1     1     1   
2     2     2   
3     3     3   
4     4     4  
```

Constant column widths
```python3
import beautiful_table

table = beautiful_table.BeautifulTable(['row name', 'col1', 'col2', 'col3'], padding=2, maxes=10)

for i in range(5):
    table.printrow([i for j in range(4)])
```
```
row name    col1        col2        col3      
0           0           0           0         
1           1           1           1         
2           2           2           2         
3           3           3           3         
4           4           4           4 
```

Individual column widths
```python3
import beautiful_table

table = beautiful_table.BeautifulTable(['row name', 'col1', 'col2', 'col3'], padding=3, maxes=[10, 5, 5, 5])

for i in range(5):
    table.printrow([i for j in range(4)])
```
```
row name     col1    col2    col3 
0            0       0       0    
1            1       1       1    
2            2       2       2    
3            3       3       3    
4            4       4       4  
```

Custom column dividers
```python3
import beautiful_table

table = beautiful_table.BeautifulTable(['row name', 'col1', 'col2', 'col3'], padding=2, maxes=10, split='|')

for i in range(5):
    table.printrow([i for j in range(4)])
```
```
row name   |col1       |col2       |col3      
0          |0          |0          |0         
1          |1          |1          |1         
2          |2          |2          |2         
3          |3          |3          |3         
4          |4          |4          |4
```
