
row_separator = ";"
column_separator = ","



def print_board(input_string):
    # Split the string into rows
    rows = input_string.split(row_separator)
    # Split each row into columns, creating a list of lists
    list_of_lists = [row.split(column_separator) for row in rows]
    return list_of_lists



def find_head(list_of_lists):
    for row_index in range(len(list_of_lists)):
        row = list_of_lists[row_index]
        for col_index in range(len(row)):
            if row[col_index] == '*':
                return row_index, col_index
    return None