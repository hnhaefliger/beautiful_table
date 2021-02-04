# beautiful_table
Print table-like data one row at a time in python without the formatting and alignment annoyances

´´´python3
import beautiful_table

table = beautiful_table.BeautifulTable(['col1', 'col2', 'col3'])

for i in range(10):
  table.printrow([i for j in range(3)])
´´´
