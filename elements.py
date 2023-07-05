from base import pos_to_sqr
import numpy as np

class Player() : 
    def __init__(self) : 
        pass
    pass


class Piece : 
    def __init__(self, position, color) : 
        self.position = position
        self.color = color
        pass
    def __str__(self) : 
        return "Piece"

class Pawn(Piece) : 
    def __init__(self, position, color) : 
        super().__init__(position, color) 
        self.new = True

    def __str__(self) : 
        return "Pawn"

class Rook(Piece) : 
    def __init__(self, position, color) : 
        super().__init__(position, color) 

    def __str__(self) : 
        return "Rook"

class Bishop(Piece) : 
    def __init__(self, position, color) : 
        super().__init__(position, color) 

    def __str__(self) : 
        return "Bishop"

class Knight(Piece) : 
    def __init__(self, position, color) : 
        super().__init__(position, color) 

    def __str__(self) : 
        return "Knight"

class Queen(Piece) : 
    def __init__(self, position, color) : 
        super().__init__(position, color) 

    def __str__(self) : 
        return "Queen"

class King(Piece) : 
    def __init__(self, position, color) : 
        super().__init__(position, color) 

    def __str__(self) : 
        return "King"
    


class White (Player) : 
    def __init__(self):
        super().__init__() 
        self.turn = 0
        self.pawn1 = Pawn("a2", "white")
        self.pawn2 = Pawn("b2", "white")
        self.pawn3 = Pawn("c2", "white")
        self.pawn4 = Pawn("d2", "white")
        self.pawn5 = Pawn("e2", "white")
        self.pawn6 = Pawn("f2", "white")
        self.pawn7 = Pawn("g2", "white")
        self.pawn8 = Pawn("h2", "white")
        self.rook1 = Rook("a1", "white")
        self.rook2 = Rook("h1", "white")
        self.knight1 = Knight("b1", "white")
        self.knight2 = Knight("g1", "white")
        self.bishop1 = Bishop("c1", "white")
        self.bishop2 = Bishop("f1", "white")
        self.queen = Queen("d1", "white")
        self.king = King("e1", "white")

    def dic_of_pieces(self) : 
        return {v : k for v, k in vars(self).items() if v != "turn"} 

    def dic_of_positions(self) : 
        return {v : k.position for v, k in vars(self).items() if v != "turn"} 

    def dic_of_squares(self) : 
        return {v : pos_to_sqr(k.position) for v, k in vars(self).items() if v != "turn"} 
    
    def __str__(self) : 
        return "white"

class Black(Player) : 
    def __init__(self):
        super().__init__()
        self.turn = 1
        self.pawn1 = Pawn("a7", "black")
        self.pawn2 = Pawn("b7", "black")
        self.pawn3 = Pawn("c7", "black")
        self.pawn4 = Pawn("d7", "black")
        self.pawn5 = Pawn("e7", "black")
        self.pawn6 = Pawn("f7", "black")
        self.pawn7 = Pawn("g7", "black")
        self.pawn8 = Pawn("h7", "black")
        self.rook1 = Rook("a8", "black")
        self.rook2 = Rook("h8", "black")
        self.knight1 = Knight("b8", "black")
        self.knight2 = Knight("g8", "black")
        self.bishop1 = Bishop("c8", "black")
        self.bishop2 = Bishop("f8", "black")
        self.queen = Queen("d8", "black")
        self.king = King("e8", "black")

    def dic_of_pieces(self) : 
        return {v : k for v, k in vars(self).items() if v != "turn"} 

    def dic_of_positions(self) : 
        return {v : k.position for v, k in vars(self).items() if v != "turn"} 

    def dic_of_squares(self) : 
        return {v : pos_to_sqr(k.position) for v, k in vars(self).items() if v != "turn"}   
    
    def __str__(self) : 
        return "black"
    



class Board() : 
    def __init__(self) : 

        self.rows = [str(a) for a in range(1, 8)]
        self.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.positions = [[f"{a}{b}" for a in self.columns] for b in self.rows]
        self.squares = np.array([ [0 for i in range(8) ] for i in range(8)])
    pass
        
class Game() : 
    def __init__(self, board : Board, white : White, black : Black ) : 
        self.white = white
        self.black = black
        self.board = board
        self.highlights = []

        for player in [self.white, self.black] : 
            print(player.dic_of_squares().items())
            for _, position in player.dic_of_squares().items() :
                x, y = position
                self.board.squares[x][y] = 1
        

    def actualize(self) : 
        self.board.squares = [[0 for _ in range(8)] for _ in range(8)]
        for player in [self.white, self.black] : 
            print(player.dic_of_squares().items())
            for _, position in player.dic_of_squares().items() :
                x, y = position
                self.board.squares[x][y] = 1




if __name__ == "__main__" : 
    b = Black()
    w = White()
    board = Board()
    game = Game(board, w, b)

    print(game.board.squares)
    

