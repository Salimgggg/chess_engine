import tkinter as tk
import elements as e
import game as g
# Define the dimensions of the chessboard
BOARD_SIZE = 8
SQUARE_SIZE = 60
WINDOW_SIZE = BOARD_SIZE * SQUARE_SIZE

def convert_coordinates(x, y):
    """Convert bottom-left-based coordinates to tkinter coordinates."""
    tkinter_y = BOARD_SIZE - y - 1
    return x, tkinter_y

image_paths = {"White_Pawn" : "/white_pawn.png",
               "White_Bishop" : "/white_bishop.png",
               "White_Rook" : "/white_rook.png", 
               "White_Knight" : "/white_knight.png", 
               "White_King" : "/white_king.png", 
               "White_Queen" : "/white_queen.png", 
               "Black_Pawn" : "/black_pawn.png", 
               "Black_Bishop" : "/black_bishop.png" , 
               "Black_Rook" : "/black_rook.png",
               "Black_Knight" : "/black_knight.png",
               "Black_King" : "/black_king.png",
               "Black_Queen" : "/black_queen.png",
}


def display_piece(canvas, position, image):
    x = position[0] * SQUARE_SIZE + SQUARE_SIZE // 2
    y = (BOARD_SIZE - 1 - position[1]) * SQUARE_SIZE + SQUARE_SIZE // 2
    canvas.create_image(x, y, image=image)

# Function to display the board squares
def display_game(window, canvas, game):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            trace_col, trace_row = convert_coordinates(col, row)
            x1 = trace_col * SQUARE_SIZE
            y1 = trace_row * SQUARE_SIZE
            x2 = x1 + SQUARE_SIZE
            y2 = y1 + SQUARE_SIZE
            if (col, row) in game.highlights : 
                color = "green" 
            else : 
                color = "white" if (row + col) % 2 == 0 else "gray"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    player_1 = game.white
    player_2 = game.black

    root = "./piece_images"
    images = {}  # Dictionary to store the PhotoImage objects

    for player in [player_1, player_2]:
        color = str(player)

        for _, piece in player.dic_of_pieces().items():
            position = e.pos_to_sqr(piece.position)
            name_piece = str(piece).lower()
            path = root + f"/{color}_{name_piece}.png"
            print(piece, position, path)

            # Create the PhotoImage object for each piece and store it in the dictionary
            if path not in images:
                images[path] = tk.PhotoImage(file=path).subsample(2)

            display_piece(canvas, position, images[path])

    window.mainloop()
    

if __name__ == "__main__" : 
    window = tk.Tk()
    window.title("Chess Game")
    canvas = tk.Canvas(window, width=WINDOW_SIZE, height=WINDOW_SIZE)
    canvas.pack()

    w = e.White()
    b = e.Black()
    w.pawn1.position = "a4"
    board = e.Board()
    game = e.Game(board, w, b)
    highlights = g.knight_of_pos((2, 2), game)
    print(highlights)
    game.highlights = highlights

    display_game(window, canvas, game )

    pass