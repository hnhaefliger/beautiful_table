class BeautifulTable:
    '''
    Class for printing table-like data
    '''
    def __init__(self, cols, padding=2, maxes=None):
        '''
        Define maximum column widths based on datatype and print column titles
        '''
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
        '''
        Print a row from the table
        '''
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
