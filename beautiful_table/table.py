class BeautifulTable:
    def __init__(self, cols, padding=2, maxes=None):
        if maxes == None:
            self.maxes = [len(col) for col in cols]

        elif type(maxes) == int:
            self.maxes = [maxes for col in cols]

        else:
            if hasattr(maxes, '__getitem__') and type(maxes) != str:
                if len(maxes) == len(cols):
                    self.maxes = maxes

                else:
                    raise IndexError('Must provide a maximum length for each column')

            else:
                raise TypeError('Invalid type passed for max column width')

        self.padding = padding
        self.cols = cols

        self.printrow(cols)

    def printrow(self, row):
        if hasattr(row, '__getitem__') and type(row) != str:
            if len(row) != len(self.cols):
                raise IndexError('Row dimensions must match table dimensions')

        else:
            raise TypeError('Invalid type passed for row')

        row = [str(item) for item in row]
        
        row = [row[i] + ' '*(self.maxes[i] - len(row[i])) for i in range(len(row))]
        row = [row[i][:self.maxes[i]] for i in range(len(row))]
        row = (' '*self.padding).join(row)

        print(row)

test = BeautifulTable(['a', 'asjndaj', 'ajnsdjas'], padding=5, maxes=[2, 2, 2])

for i in range(10):
    test.printrow([i, i, i])
