import elements as e
import base as b
import numpy as np

def inbound(position) : 
    x, y = position
    return (0 <= x <= 7) and (0 <= y <= 7)

def row_of_pos (position, game : e.Game) : 
    x, y = position
    incr = [(i, 0) for i in range(-7, 8) ]
    extended_row = [(x1 + x, y1 + y) for x1, y1 in incr]
    real_row = list(filter(inbound, extended_row))
    
    return real_row

def col_of_pos (position, game : e.Game) : 
    x, y = position
    incr = [(0, i) for i in range(-7, 8)]
    extended_col = [(x1 + x, y1 + y) for x1, y1 in incr]
    real_col = list(filter(inbound, extended_col))

    return real_col


def diag_of_pos(position, game: e.Game) : 
    x, y = position
    incr = [(i, i) for i in range(-7, 8)]
    anti_incr = [(-i, i) for i in range(-7, 8)]
    all_incr = incr + anti_incr
    extended_diag = [(x1 + x, y1 + y) for x1, y1 in all_incr]
    real_diag = list(filter(inbound, extended_diag))

    return real_diag
    

def knight_of_pos (position, game : e.Game) : 
    incr = [(1, 2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, -1), (-2, 1), (1, -2)]
    x, y = position
    extended_knight = [(x1 + x, y1 + y) for x1, y1 in incr]
    real_knight = list(filter(inbound, extended_knight))
    return real_knight

def accessible_pawn(piece : e.Pawn, game : e.Game) : 
    possible = np.array([[1 for _ in range(8) ] for _ in range(8)])

    position = b.pos_to_sqr(piece.position)

    increments = [(0, 1)]
    if piece.new : 
        increments.append((0, 2))
    else : 
        pass 

    color = piece.color 

    if color == "black" : 
        increments = [tuple(-x for x in original) for original in increments]

    for inc in increments : 
        new = tuple(x + y for x, y in zip(inc, position))
        x, y = new 
        print(new)
        if inbound(new) : 
            possible[x][y] = 0

    return np.bitwise_or(possible, game.board.squares)


def move(game, piece, new_position) : 
    piece.position = new_position
    game.actualize()




if __name__ == "__main__" :
    black = e.Black()
    white = e.White()
    board = e.Board()
    game = e.Game(board, white, black)
    print(b.positions)
    print(b.pos_to_sqr("e3"))
    print(b.sqr_to_pos((4, 2)))
    move(game, white.pawn1, "a3")
    print (row_of_pos((0, 1), game))


