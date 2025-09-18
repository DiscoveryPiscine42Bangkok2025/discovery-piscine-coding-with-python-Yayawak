def parse_board(board_text):
    lines = board_text.splitlines()
    grid = []
    for line in lines:
        if line.strip():
            row = list(line.rstrip('\n'))
            grid.append(row)
    
    return grid

def find_king(grid):
    king_row = None
    king_col = None
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'K':
                if king_row is not None:
                    raise ValueError("Too many Kings")
                king_row = row
                king_col = col
    
    if king_row is None:
        raise ValueError("No King found")
    
    return king_row, king_col

def is_square_board(grid):
    if not grid:
        return False
    
    size = len(grid)
    for row in grid:
        if len(row) != size:
            return False
    
    return True

def is_valid_position(size, row, col):
    return 0 <= row < size and 0 <= col < size

def check_pawns(grid, king_row, king_col):
    size = len(grid)
    
    #  Left diagonal
    pawn_row = king_row + 1
    pawn_col = king_col - 1
    if is_valid_position(size, pawn_row, pawn_col):
        if grid[pawn_row][pawn_col] == 'P':
            return True
    
    # Right diagonal
    pawn_row = king_row + 1
    pawn_col = king_col + 1
    if is_valid_position(size, pawn_row, pawn_col):
        if grid[pawn_row][pawn_col] == 'P':
            return True
    
    return False

# R, B, Q
def check_line_pieces(grid, king_row, king_col):
    size = len(grid)
    
    # Check all 8 directions
    directions = [
        # up-left, up, up-right
        (-1, -1), 
        (-1, 0), 
        (-1, 1),

        # left, right
        (0, -1),
        (0, 1),

        # down-left, down, down-right
        (1, -1),  
        (1, 0),  
        (1, 1)
    ]
    
    for row_dir, col_dir in directions:
        row = king_row + row_dir
        col = king_col + col_dir
        
        while is_valid_position(size, row, col):
            piece = grid[row][col]
            
            if piece != '.':
                if piece == 'Q':
                    return True
                elif piece == 'R' and (row_dir == 0 or col_dir == 0):
                    return True
                elif piece == 'B' and row_dir != 0 and col_dir != 0:
                    return True
                else:
                    break
            
            row += row_dir
            col += col_dir
    
    return False

def is_king_in_check(grid):
    king_row, king_col = find_king(grid)
    
    if check_pawns(grid, king_row, king_col):
        return True
    
    if check_line_pieces(grid, king_row, king_col):
        return True
    
    return False


def checkmate(board_text):
    try:
        grid = parse_board(board_text)

        if not is_square_board(grid):
            print("Error")
            return

        find_king(grid)
        
        if is_king_in_check(grid):
            print("Success")
        else:
            print("Fail")
    except:
        print("Error")
