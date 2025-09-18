from checkmate import checkmate

def main():
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)
    board = """\
R...
....
..PK
....\
"""
    checkmate(board)

if __name__ == "__main__":
    main()