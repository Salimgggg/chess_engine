rows = [str(a) for a in range(1, 8)]
columns = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7}
reverse_columns = { v : k for k, v in columns.items()}
positions = [[f"{a}{b}" for a in columns.keys()] for b in rows]
squares = [ [None for i in range(7) ] for i in range(7)]

def pos_to_sqr (position) :
    position = list(position)
    column = columns[position[0]]
    row = int(position[1]) - 1
    return (column, row)

def sqr_to_pos (square) : 
    column, row = square
    column = reverse_columns[column]
    row += 1
    return f"{column}{row}"

